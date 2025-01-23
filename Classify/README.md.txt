2. Klasifikasi Apple (classify.py)
Keterangan
Program classify.py:
- Menggunakan API Roboflow untuk mendeteksi apel pada gambar tertentu.
- Mengklasifikasikan apel menjadi tiga kategori: merah, kuning, dan hijau.
- Memotong setiap apel yang terdeteksi dan menyimpannya sebagai gambar terpisah di direktori diklasifikasikan_apel.
**Cara Menggunakan**
1. Tempatkan gambar classify.jpg (atau gambar Anda sendiri) di direktori yang sama dengan classify.py.
2. Perbarui variabel berikut dalam skrip jika diperlukan:
 - Kunci API: Ganti placeholder YOUR_API_KEY dengan kunci API Roboflow Anda.
 - ID Model: Ganti placeholder YOUR_MODEL_ID dengan ID model yang sesuai.
3. Jalankan skripnya:
  python mengklasifikasikan.py
4. Program ini akan:
 - Simpan gambar potongan apel yang terdeteksi ke dalam direktori diklasifikasikan_apel.
 - Beri nama file berdasarkan warna dan urutan apel, misalnya red_1.jpg, yellow_2.jpg.
**Contoh Keluaran**
Gambar yang dipotong disimpan di direktori diklasifikasikan_apel dengan nama file seperti:
- red_1.jpg, red_2.jpg (apel merah)
- yellow_1.jpg, yellow_2.jpg (apel kuning)
- green_1.jpg (apel hijau)