from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
import os
import pickle

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # ⬅️ penting untuk konsistensi

# === Load Model dan Label ===
model = load_model("model/inception_model.h5")
with open("model/class_labels.pkl", "rb") as f:
    class_indices = pickle.load(f)
class_labels = {v: k for k, v in class_indices.items()}

# === Fungsi Prediksi ===
def prediksi_gambar(filepath):
    try:
        img = image.load_img(filepath, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Normalisasi

        pred = model.predict(img_array)[0]
        predicted_index = np.argmax(pred)
        predicted_label = class_labels[predicted_index]
        confidence = float(pred[predicted_index])
        return predicted_label, confidence

    except Exception as e:
        print(f"Error saat prediksi: {e}")
        return "Terjadi Error", 0.0

# === Halaman Utama ===
@app.route('/')
def index():
    return render_template('index.html')

# === Route Prediksi ===
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', prediction="Tidak ada file diupload.")

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', prediction="File belum dipilih.")

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        prediction, confidence = prediksi_gambar(filepath)
        return render_template('index.html', prediction=prediction, confidence=confidence, filename=file.filename)

    return render_template('index.html', prediction="Terjadi kesalahan.")

if __name__ == '__main__':
    app.run(debug=True)