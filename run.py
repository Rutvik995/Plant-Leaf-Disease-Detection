import os
import sys
import webbrowser
import threading
import time

def open_browser():
    time.sleep(2.0)
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    print("=" * 60)
    print(" Starting FloraScan AI - Plant Leaf Disease Diagnostic Server")
    print(" Model: plant_model.keras (MobileNetV2, 2.3M parameters)")
    print(" Server URL: http://127.0.0.1:5000")
    print("=" * 60)
    
    threading.Thread(target=open_browser, daemon=True).start()
    
    from app import app
    app.run(host="127.0.0.1", port=5000, debug=False)
