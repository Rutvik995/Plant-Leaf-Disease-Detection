import os
import time
import io
import base64
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from plant_data import PLANT_CLASSES, MODEL_METRICS

app = Flask(__name__)

# Load Keras Model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "plant_model.keras")
print(f"[*] Loading model from {MODEL_PATH}...")
start_time = time.time()
try:
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    load_duration = round(time.time() - start_time, 3)
    print(f"[+] Model loaded successfully in {load_duration}s!")
except Exception as e:
    print(f"[!] Error loading model: {e}")
    model = None


def preprocess_image(image_bytes):
    """Preprocesses raw bytes into a (1, 160, 160, 3) numpy array."""
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = img.resize((160, 160), Image.Resampling.BILINEAR)
    img_array = np.array(img, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, 160, 160, 3)
    return img_array


def softmax(x):
    """Computes softmax values for a score vector."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/model-info", methods=["GET"])
def get_model_info():
    """Returns technical metadata, benchmark accuracy, and parameter breakdown."""
    info = dict(MODEL_METRICS)
    info["is_model_loaded"] = (model is not None)
    return jsonify(info)


@app.route("/api/classes", methods=["GET"])
def get_classes():
    """Returns the complete list of 39 plant species and disease classes."""
    classes_list = []
    for idx, info in sorted(PLANT_CLASSES.items()):
        classes_list.append({
            "class_index": idx,
            "name": info.get("name", f"Class {idx}"),
            "plant": info.get("plant", "Unknown"),
            "condition": info.get("condition", "Unknown"),
            "status": info.get("status", "Unknown"),
            "severity": info.get("severity", "Unknown"),
            "description": info.get("description", ""),
            "symptoms": info.get("symptoms", []),
            "treatment": info.get("treatment", "")
        })
    return jsonify({"classes": classes_list, "total": len(classes_list)})


@app.route("/api/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model is not loaded."}), 500

    image_bytes = None
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            image_bytes = file.read()
    elif request.is_json:
        data = request.get_json()
        if 'image' in data:
            base64_str = data['image']
            if ',' in base64_str:
                base64_str = base64_str.split(',')[1]
            image_bytes = base64.b64decode(base64_str)

    if not image_bytes:
        return jsonify({"error": "No image file or base64 data provided."}), 400

    try:
        t0 = time.time()
        tensor_input = preprocess_image(image_bytes)

        # Run inference
        preds = model.predict(tensor_input, verbose=0)[0]
        inference_latency_ms = round((time.time() - t0) * 1000, 2)

        # Normalize outputs to probabilities (0-100%)
        # Note: Model output layer is Sigmoid over 39 classes
        if np.sum(preds) > 0:
            probs = preds / np.sum(preds)
        else:
            probs = softmax(preds)

        top_idx = int(np.argmax(probs))
        top_confidence = float(probs[top_idx])

        # Get details for top prediction
        top_info = PLANT_CLASSES.get(top_idx, {
            "name": f"Class {top_idx}",
            "plant": "Unknown",
            "condition": "Unknown",
            "status": "Unknown",
            "severity": "Unknown",
            "description": "No description available.",
            "symptoms": [],
            "treatment": "No treatment information."
        })

        # Top 5 distribution
        sorted_indices = np.argsort(probs)[::-1]
        top5 = []
        for rank, idx in enumerate(sorted_indices[:5]):
            c_info = PLANT_CLASSES.get(int(idx), {})
            top5.append({
                "rank": rank + 1,
                "class_index": int(idx),
                "name": c_info.get("name", f"Class {idx}"),
                "plant": c_info.get("plant", "Unknown"),
                "condition": c_info.get("condition", "Unknown"),
                "status": c_info.get("status", "Unknown"),
                "probability": round(float(probs[idx]) * 100, 2),
                "raw_score": float(preds[idx])
            })

        # Full 39 class breakdown
        all_classes = []
        for idx in range(len(probs)):
            c_info = PLANT_CLASSES.get(idx, {})
            all_classes.append({
                "class_index": idx,
                "name": c_info.get("name", f"Class {idx}"),
                "probability": round(float(probs[idx]) * 100, 2)
            })

        response = {
            "success": True,
            "prediction": {
                "class_index": top_idx,
                "name": top_info["name"],
                "plant": top_info["plant"],
                "condition": top_info["condition"],
                "status": top_info["status"],
                "severity": top_info["severity"],
                "confidence_percent": round(top_confidence * 100, 2),
                "raw_activation": float(preds[top_idx]),
                "description": top_info["description"],
                "symptoms": top_info["symptoms"],
                "treatment": top_info["treatment"]
            },
            "top5_distribution": top5,
            "all_classes": all_classes,
            "performance": {
                "inference_latency_ms": inference_latency_ms,
                "model_architecture": MODEL_METRICS["architecture"],
                "input_tensor_shape": [1, 160, 160, 3],
                "benchmark_accuracy": MODEL_METRICS["benchmark_accuracy"]
            }
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": f"Inference error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
