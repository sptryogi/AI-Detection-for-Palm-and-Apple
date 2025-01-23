import streamlit as st
import cv2
import numpy as np
from PIL import Image
from inference_sdk import InferenceHTTPClient
import tempfile

# Inisialisasi Roboflow Client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="xzMdQBu3cn7VC7X1ZNeK"  # API Key Anda
)

# Model IDs
PALM_TREE_MODEL = "palm-tree-c56ky/52"
APPLE_CLASSIFY_MODEL = "apple_maturity-1ayzw/1"
CONFIDENCE_THRESHOLD = 0.5  # Confidence minimal

# Fungsi Resize Gambar
def resize_image(image, size=(1024, 1024)):
    original_width, original_height = image.size
    resized_img = image.resize(size)
    return resized_img, original_width, original_height

# Fungsi untuk menggambar bounding box pada Palm Tree Detection
def draw_palm_boxes(image, detections, original_width, original_height, input_width, input_height):
    img = np.array(image)
    x_scale = original_width / input_width
    y_scale = original_height / input_height

    for i, detection in enumerate(detections):
        if detection["confidence"] < CONFIDENCE_THRESHOLD:
            continue
        x, y, w, h = detection["x"], detection["y"], detection["width"], detection["height"]
        x = int(x * x_scale)
        y = int(y * y_scale)
        w = int(w * x_scale)
        h = int(h * y_scale)
        x_min, y_min = x - w // 2, y - h // 2
        x_max, y_max = x + w // 2, y + h // 2
        cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 3)
        cv2.putText(img, f"{i + 1}", (x_min, y_min - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    total_objects_text = f"Total Palm Trees: {len(detections)}"
    cv2.putText(img, total_objects_text, (10, img.shape[0] - 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
    return img

# Fungsi untuk memotong gambar apel berdasarkan klasifikasi
def crop_apples(image, detections, original_width, original_height, input_width, input_height):
    x_scale = original_width / input_width
    y_scale = original_height / input_height

    cropped_images = []
    for i, detection in enumerate(detections):
        if detection["confidence"] < CONFIDENCE_THRESHOLD:
            continue
        x, y, w, h = detection["x"], detection["y"], detection["width"], detection["height"]
        x = int(x * x_scale)
        y = int(y * y_scale)
        w = int(w * x_scale)
        h = int(h * y_scale)
        x_min, y_min = x - w // 2, y - h // 2
        x_max, y_max = x + w // 2, y + h // 2

        crop = image.crop((x_min, y_min, x_max, y_max))
        label = detection["class"]
        cropped_images.append((crop, label, i + 1))

    return cropped_images

# Fungsi Inferensi
def process_image(image, model_id):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        image.save(temp_file.name)
        result = CLIENT.infer(temp_file.name, model_id=model_id)
        detections = result["predictions"]
        input_width = result["image"]["width"]
        input_height = result["image"]["height"]
    return detections, input_width, input_height

# Streamlit App
def main():
    st.title("AI Detection Web App")
    st.sidebar.title("Pilih Fitur")
    option = st.sidebar.selectbox("Menu", ["Count Palm Trees", "Classify Apples"])

    if option == "Count Palm Trees":
        st.header("Palm Tree Detection")
        uploaded_file = st.file_uploader("Unggah Gambar (Palm Trees)", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Gambar Awal", use_column_width=True)

            resized_image, original_width, original_height = resize_image(image)
            st.write("Gambar sedang diproses, harap tunggu...")
            try:
                detections, input_width, input_height = process_image(resized_image, PALM_TREE_MODEL)
                output_img = draw_palm_boxes(image, detections, original_width, original_height, input_width, input_height)
                st.image(output_img, caption="Hasil Deteksi", use_column_width=True)
                st.success(f"Deteksi selesai! Total pohon kelapa sawit: {len(detections)}")
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")

    elif option == "Classify Apples":
        st.header("Apple Classification")
        uploaded_file = st.file_uploader("Unggah Gambar (Apples)", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Gambar Awal", use_column_width=True)

            resized_image, original_width, original_height = resize_image(image)
            st.write("Gambar sedang diproses, harap tunggu...")
            try:
                detections, input_width, input_height = process_image(resized_image, APPLE_CLASSIFY_MODEL)
                cropped_images = crop_apples(image, detections, original_width, original_height, input_width, input_height)

                st.write("Hasil Klasifikasi:")
                for crop, label, index in cropped_images:
                    st.image(crop, caption=f"{label}_{index}", use_column_width=False)
                    crop.save(f"{label}_{index}.jpg")
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
