import pytesseract
from PIL import Image
import os

# (Only for Windows: Set path to tesseract executable)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_text(image_path):
    """Recognizes text from the given image using OCR."""
    if not os.path.exists(image_path):
        print(f"Error: Image '{image_path}' not found.")
        return "No text detected."

    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        text = text.strip()

        with open("recognized_text.txt", "w") as f:
            f.write(text)

        return text if text else "No text detected."
    except Exception as e:
        print(f"OCR Error: {e}")
        return "No text detected."

if __name__ == "__main__":
    text = recognize_text("captured_image.jpg")
    print("Recognized Text:", text)
