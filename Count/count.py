from inference_sdk import InferenceHTTPClient
import cv2
import os

# Inisialisasi Roboflow Client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="xzMdQBu3cn7VC7X1ZNeK"  # Ganti dengan API Key Anda
)

MODEL_ID = "palm-tree-c56ky/52"  # ID model dari Roboflow
CONFIDENCE_THRESHOLD = 0.5  # Threshold confidence minimum


# Fungsi untuk resize gambar ke 1024x1024
def resize_image(image_path, size=(1024, 1024)):
    img = cv2.imread(image_path)
    original_height, original_width = img.shape[:2]
    resized_img = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    return resized_img, original_width, original_height


# Fungsi untuk menggambar bounding box dengan nomor objek
def draw_bounding_boxes(image, detections, original_width, original_height, input_width, input_height):
    # Sesuaikan skala bounding box ke ukuran asli
    x_scale = original_width / input_width
    y_scale = original_height / input_height

    for i, detection in enumerate(detections):
        if detection["confidence"] < CONFIDENCE_THRESHOLD:
            continue  # Abaikan jika confidence lebih kecil dari threshold

        x, y, w, h = detection["x"], detection["y"], detection["width"], detection["height"]

        # Konversi koordinat berdasarkan skala asli
        x = int(x * x_scale)
        y = int(y * y_scale)
        w = int(w * x_scale)
        h = int(h * y_scale)

        # Hitung koordinat bounding box
        x_min, y_min = x - w // 2, y - h // 2
        x_max, y_max = x + w // 2, y + h // 2

        # Gambar bounding box pada gambar asli
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 3)  # Ketebalan lebih besar (3)

        # Tambahkan nomor objek
        cv2.putText(image, f"{i + 1}", (x_min, y_min - 15),  # Perbesar jarak teks
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)  # Perbesar font dan ketebalan

    # Tambahkan teks jumlah total objek
    total_objects_text = f"Total Objects: {len(detections)}"
    cv2.putText(image, total_objects_text, (10, original_height - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)  # Perbesar font dan ketebalan teks

    return image


# Fungsi untuk memproses gambar dan melakukan inferensi
def process_image(image_path, model_id):
    try:
        print("[INFO] Membaca dan mengirim gambar ke API...")

        # Resize gambar ke 1024x1024 sebelum dikirim
        resized_image, original_width, original_height = resize_image(image_path)
        resized_path = "resized_" + os.path.basename(image_path)
        cv2.imwrite(resized_path, resized_image)

        # Kirim gambar ke Roboflow API
        result = CLIENT.infer(resized_path, model_id=model_id)
        detections = result["predictions"]
        input_width = result["image"]["width"]
        input_height = result["image"]["height"]

        print(f"[INFO] Jumlah deteksi: {len(detections)}")

        # Baca gambar asli dan gambarkan bounding box
        original_image = cv2.imread(image_path)
        output_image = draw_bounding_boxes(original_image, detections, original_width, original_height, input_width, input_height)

        # Simpan hasil output
        output_path = "output_" + os.path.basename(image_path)
        cv2.imwrite(output_path, output_image)
        print(f"[INFO] Gambar hasil disimpan di: {output_path}")

        # Tampilkan hasil
        cv2.imshow("Deteksi Palm Tree", output_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")


# Main Program
if __name__ == "__main__":
    # Ganti path gambar dengan file input Anda
    IMAGE_PATH = "count.jpeg"  # Path ke file gambar input
    process_image(IMAGE_PATH, MODEL_ID)
