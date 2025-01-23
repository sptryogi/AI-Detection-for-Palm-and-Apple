# AI-Detection-for-Palm-and-Apple
## Deskripsi
**AI Detection** adalah aplikasi berbasis web untuk mendeteksi objek menggunakan model deteksi berbasis **Roboflow API**. Aplikasi ini memiliki dua fitur utama:  
1. **Count Palm Trees**: Mendapatkan jumlah pohon kelapa sawit dalam gambar dengan bounding box dan nomor urut.  
2. **Classify Apples**: Mengklasifikasikan apel berdasarkan warna (merah, kuning, hijau) dan menghasilkan potongan gambar setiap apel.

## Fitur
- **Count Palm Trees**:  
  - Menampilkan bounding box pada setiap pohon kelapa sawit yang terdeteksi.  
  - Menampilkan jumlah total pohon kelapa sawit di gambar.  
- **Classify Apples**:  
  - Mengklasifikasikan apel berdasarkan warna (red, yellow, green).  
  - Menyimpan potongan gambar apel dengan nama file sesuai klasifikasinya (misalnya: `red_1.jpg`).

---

## Cara Install dan Menjalankan

### 1. **Prasyarat**
- **Python 3.8 atau lebih baru** harus terinstal.
- Install pustaka yang diperlukan:
  ```bash
  pip install streamlit pillow opencv-python-headless inference-sdk
  ```

### 2. **Clone Repository**
```bash
git clone https://github.com/username/ai-detection-web-app.git
cd ai-detection-web-app
```

### 3. **Menyiapkan API Key**
- Daftar ke **Roboflow** di [https://roboflow.com](https://roboflow.com).
- Dapatkan **API Key** Anda.
- Ganti placeholder `xzMdQBu3cn7VC7X1ZNeK` pada file `app.py` dengan API Key Anda.

### 4. **Menjalankan Aplikasi**
Jalankan aplikasi Streamlit:
```bash
streamlit run app.py
```

---

## Cara Penggunaan
1. **Count Palm Trees**
   - Unggah gambar pohon kelapa sawit melalui halaman aplikasi.
   - Aplikasi akan mendeteksi pohon kelapa sawit, menampilkan bounding box dengan nomor urut, dan menunjukkan total jumlah pohon.
   - Hasil gambar akan ditampilkan di aplikasi.

2. **Classify Apples**
   - Unggah gambar apel dengan berbagai warna.
   - Aplikasi akan mengklasifikasikan apel berdasarkan warna (merah, kuning, hijau).
   - Gambar apel yang sudah terpotong akan ditampilkan, dan file potongan disimpan dengan format `red_1.jpg`, `green_1.jpg`, dll.

---

## Struktur Proyek
```
.
├── app.py                  # File utama aplikasi Streamlit
├── requirements.txt        # File dependensi
├── README.md               # Dokumentasi proyek
```

---

## Contoh Gambar Input dan Output
### **Count Palm Trees**
#### Input:
![Palm Trees Input](example_palm_input.jpg)  
#### Output:
![Palm Trees Output](example_palm_output.jpg)

### **Classify Apples**
#### Input:
![Apples Input](example_apples_input.jpg)  
#### Output:
- `red_1.jpg`
- `green_1.jpg`
- `yellow_1.jpg`

---

## Teknologi yang Digunakan
- **Streamlit**: Untuk membangun antarmuka aplikasi berbasis web.
- **Pillow (PIL)**: Untuk manipulasi gambar.
- **OpenCV**: Untuk menggambar bounding box dan teks pada gambar.
- **Roboflow API**: Untuk inferensi deteksi dan klasifikasi objek.

---
