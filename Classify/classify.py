from inference_sdk import InferenceHTTPClient
import cv2
import os

# Inisialisasi Roboflow Client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="xzMdQBu3cn7VC7X1ZNeK"  # API Key 
)

MODEL_ID = "apple_maturity-1ayzw/1"  # ID model 

# Direktori output untuk menyimpan hasil crop
OUTPUT_DIR = "classified_apples"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Fungsi untuk memproses deteksi apel dan mengklasifikasikan berdasarkan warna
def classify_apples(image_path, model_id):
    try:
        print("[INFO] Mengirim gambar ke Roboflow API...")
        result = CLIENT.infer(image_path, model_id=model_id)

        # Dapatkan hasil deteksi
        detections = result["predictions"]

        # Baca gambar asli
        img = cv2.imread(image_path)
        original_height, original_width, _ = img.shape

        # Ambil ukuran gambar yang diproses oleh API
        input_width = result["image"]["width"]
        input_height = result["image"]["height"]

        # Sesuaikan skala bounding box ke ukuran gambar asli
        x_scale = original_width / input_width
        y_scale = original_height / input_height

        # Counters untuk setiap kategori
        counters = {"red": 0, "yellow": 0, "green": 0}

        # Iterasi setiap deteksi
        for detection in detections:
            x, y, w, h = detection["x"], detection["y"], detection["width"], detection["height"]
            color = detection["class"]  # Warna apel (red, yellow, green)

            # Pastikan deteksi hanya pada apel dengan warna yang valid
            if color not in counters:
                continue

            # Konversi koordinat berdasarkan skala
            x = int(x * x_scale)
            y = int(y * y_scale)
            w = int(w * x_scale)
            h = int(h * y_scale)

            # Hitung koordinat bounding box
            x_min, y_min = max(0, x - w // 2), max(0, y - h // 2)
            x_max, y_max = min(original_width, x + w // 2), min(original_height, y + h // 2)

            # Crop gambar berdasarkan bounding box
            cropped_img = img[y_min:y_max, x_min:x_max]

            # Simpan gambar yang terpotong dengan nama file sesuai warna dan nomor
            counters[color] += 1
            output_path = os.path.join(OUTPUT_DIR, f"{color}_{counters[color]}.jpg")
            cv2.imwrite(output_path, cropped_img)
            print(f"[INFO] Gambar apel {color} disimpan di: {output_path}")

        print("[INFO] Proses klasifikasi selesai.")
        print(f"[INFO] Total apel yang terdeteksi: Red={counters['red']}, Yellow={counters['yellow']}, Green={counters['green']}")

    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan saat inferensi: {str(e)}")


# Main
if __name__ == "__main__":
    # Path ke gambar input
    image_path = "classify.jpeg"  # Ganti dengan path gambar input 
    classify_apples(image_path, MODEL_ID)
