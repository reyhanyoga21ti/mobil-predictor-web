# Mobil Predictor Web 🚗🔍

Sebuah aplikasi web berbasis Flask yang memanfaatkan deep learning untuk memprediksi jenis mobil dari gambar. Model yang digunakan adalah InceptionV3 yang telah dilatih dengan dataset mobil dari beberapa merk.

---

## 🚀 Fitur

- Upload gambar mobil dan prediksi otomatis jenis mobilnya.
- Menampilkan confidence (tingkat keyakinan) dari prediksi.
- Antarmuka web sederhana dan responsif (HTML + CSS).
- Support model `.keras` modern.
- Ringan dan mudah dijalankan di lokal.

---

## 📂 Struktur Folder
mobil-predictor-web/
├── app.py # Aplikasi Flask utama
├── model/
│ ├── inception_model.h5 # Model deep learning (.keras)
│ └── class_labels.pkl # Label klasifikasi
├── static/
│ └── uploads/ # Tempat menyimpan gambar yang diunggah
├── templates/
│ └── index.html # Antarmuka pengguna
├── requirements.txt # Daftar dependensi Python
├── run.bat # Script untuk menjalankan aplikasi di Windows
└── README.md # Dokumentasi proyek ini

## 🛠️ Instalasi

1. **Clone repositori:**
   ```bash
   git clone https://github.com/reyhanyoga21ti/mobil-predictor-web.git
   cd mobil-predictor-web

2. Buat dan aktifkan virtual environment (Windows):
   python -m venv venv
   venv\Scripts\activate

3. Install dependensi:
   pip install -r requirements.txt

4. Pastikan file berikut sudah ada:
   model/inception_model.h5 (model prediksi mobil)
   model/class_labels.pkl (label klasifikasi)

5. Jalankan aplikasi menggunakan:
   flask run

   atau langsung dengan file batch:
   run.bat

   Lalu buka browser ke: http://127.0.0.1:5000

📸 Contoh Penggunaan
   1. Pilih file gambar mobil dari perangkat.

   2. Klik tombol Prediksi.

   3. Hasil prediksi dan confidence akan ditampilkan.

🧠 Model & Dataset
   Model: InceptionV3 dari Keras Applications.

   Input size: 224x224

   Output: 55 kelas mobil.

   Dataset: dataset public VMMRDb

📦 Requirements
   - Flask==2.3.3
   - tensorflow==2.16.1
   - keras==3.3.3
   - numpy==1.24.3
   - Pillow==10.1.0
   - werkzeug==2.3.7

   Instalasi otomatis lewat:

   pip install -r requirements.txt

🔗 Download Model dan Label
   Untuk menjalankan aplikasi prediksi, kamu perlu mengunduh file model dan label berikut ini:

   - Model InceptionV3 (.h5)

   - Label Kelas (.pkl)

➡️ Link untuk mengunduh file model & label dari Google Drive:
   https://drive.google.com/drive/folders/1emerAhFu9-W473EGmgdpO3M62RJJwbKY?usp=sharing

   Setelah diunduh, letakkan file tersebut di dalam folder model/ di dalam proyek kamu.

📌 Jika folder model/ belum ada, silakan buat folder baru dengan nama model di root proyek kamu (di samping app.py).
