# 🌱 Plant Leaf Disease Detection System

An AI-powered web application for real-time plant leaf disease detection and treatment recommendations, built with **TensorFlow / Keras (MobileNetV2)** and **Flask**.

---

## 🚀 Overview

This application helps farmers, agronomists, and gardeners diagnose plant diseases from leaf photographs. It utilizes a pre-trained **MobileNetV2** deep convolutional neural network trained on the PlantVillage dataset across **39 different plant and disease categories**. 

Along with the diagnosis and confidence level, the system provides detailed symptoms, organic/chemical treatment advice, and visual probability distributions.

---

## ✨ Features

- **High Accuracy Inference:** Powered by MobileNetV2 with a benchmark test accuracy of **97.42%**.
- **39 Plant Categories:** Classifies healthy leaves and diseases across crops like Tomato, Potato, Apple, Corn, Grape, Pepper, and more.
- **Actionable Diagnosis:** Returns disease severity, symptoms, organic treatments, and chemical control recommendations.
- **Top-5 Prediction Breakdown:** Visual probability distribution across top matching classes.
- **Modern Glassmorphic UI:** Responsive dark-mode interface with drag-and-drop file upload, real-time preview, and sample leaf test generator.
- **Fast CPU Latency:** Lightweight architecture (~2.3M parameters) executing predictions in ~14–25 ms.

---

## 📊 Model Performance & Specifications

| Property | Value / Specification |
| :--- | :--- |
| **Base Architecture** | MobileNetV2 (Functional API) |
| **Benchmark Test Accuracy** | **97.42%** |
| **Precision / Recall / F1** | 97.10% / 96.85% / 96.97% |
| **Total Parameters** | 2,307,943 (~8.80 MB weights) |
| **Input Shape** | `(160, 160, 3)` RGB |
| **Training Dataset** | PlantVillage Augmented Dataset (54,000+ images) |
| **Output Classes** | 39 classes |

---

## 📂 Project Structure

```text
├── app.py               # Flask backend API & prediction pipeline
├── plant_data.py        # Knowledge base of 39 disease classes, symptoms & remedies
├── plant_model.keras    # Pre-trained MobileNetV2 model
├── requirements.txt     # Python dependencies
├── run.py               # Application launcher
├── static/
│   ├── css/style.css    # Modern glassmorphism dark-theme styles
│   └── js/script.js     # Client-side UI interactions & API integration
└── templates/
    └── index.html       # Web dashboard template
```

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.10+** installed.

### 2. Clone the Repository
```bash
git clone https://github.com/Rutvik995/Plant-Leaf-Disease-Detection.git
cd Plant-Leaf-Disease-Detection
```

### 3. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Launch the Application
```bash
python run.py
```
Or directly via Flask:
```bash
python app.py
```

The web application will be accessible at:  
👉 **`http://127.0.0.1:5000`**

---

## 🌾 Supported Crops & Diseases

The model classifies 39 categories including:
- **Apple:** Scab, Black Rot, Cedar Apple Rust, Healthy
- **Blueberry:** Healthy
- **Cherry:** Powdery Mildew, Healthy
- **Corn (Maize):** Cercospora Leaf Spot, Common Rust, Northern Leaf Blight, Healthy
- **Grape:** Black Rot, Esca (Black Measles), Leaf Blight, Healthy
- **Orange:** Citrus Greening (Huanglongbing)
- **Peach:** Bacterial Spot, Healthy
- **Pepper Bell:** Bacterial Spot, Healthy
- **Potato:** Early Blight, Late Blight, Healthy
- **Raspberry:** Healthy
- **Soybean:** Healthy
- **Squash:** Powdery Mildew
- **Strawberry:** Leaf Scorch, Healthy
- **Tomato:** Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
