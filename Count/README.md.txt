1. Penghitungan Pohon Palem (count.py)
Keterangan
Program count.py:
- Menggunakan API Roboflow untuk mendeteksi pohon palem pada gambar udara tertentu.
- Menghitung jumlah pohon palem.
- Menggambar kotak pembatas dengan ID unik untuk setiap pohon yang terdeteksi.
- Menyimpan gambar beranotasi sebagai output.jpg.
**Cara Menggunakan**
1. Tempatkan gambar yang ingin Anda analisis di direktori yang sama dengan count.py.
2. Perbarui variabel berikut dalam skrip jika diperlukan:
 - Kunci API: Ganti placeholder YOUR_API_KEY dengan kunci API Roboflow Anda.
 - ID Model: Ganti placeholder YOUR_MODEL_ID dengan ID model yang sesuai.
3. Jalankan skripnya:
   python count.py
4. Program ini akan:
- Menampilkan jumlah pohon palem yang terdeteksi.
- Simpan gambar beranotasi sebagai output.jpg di direktori yang sama.
**Contoh Keluaran**
- Gambar beranotasi dengan kotak pembatas untuk setiap pohon palem yang terdeteksi dan ID unik.
- Output konsol menunjukkan jumlah total, misalnya 300 pohon palem terdeteksi.