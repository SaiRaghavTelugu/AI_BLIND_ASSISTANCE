import tkinter as tk
from tkinter import messagebox
from PIL import Image
from translation_tts_module import translate_text, speak_text
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import os
import cv2  # OpenCV for real-time image capture

# Force CPU
device = torch.device("cpu")

# Load BLIP base model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=True)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

def format_description(scene_text):
    """Generate structured scene description."""
    description = f"Scene shows {scene_text}."
    return description

def describe_scene(image_path, language_code):
    """Generate scene description, translate to the selected language, and speak."""
    if not os.path.exists(image_path):
        messagebox.showerror("Error", f"Image '{image_path}' not found.")
        return "Image not found."

    try:
        image = Image.open(image_path).convert("RGB")
        image = image.resize((384, 384))  # Resize image to reduce memory
        inputs = processor(images=image, return_tensors="pt").to(device)
        output = model.generate(**inputs)
        scene_text = processor.batch_decode(output, skip_special_tokens=True)[0]
    except Exception as e:
        messagebox.showerror("Error", f"Scene description error: {e}")
        scene_text = "A generic scene"

    english_description = format_description(scene_text)

    try:
        translated_description = translate_text(english_description, target_language=language_code)
    except Exception as e:
        messagebox.showerror("Error", f"Translation error: {e}")
        translated_description = "Translation error."

    # Save description to file
    with open("scene_description.txt", "w", encoding="utf-8") as file:
        file.write(translated_description)

    # Speak the description
    speak_text(translated_description, language=language_code)

    return translated_description

def capture_image():
    """Capture an image using the webcam."""
    cap = cv2.VideoCapture(0)  # Open the default camera
    if not cap.isOpened():
        messagebox.showerror("Error", "Unable to access the camera.")
        return

    messagebox.showinfo("Info", "Press 'Space' to capture the image and 'Esc' to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Failed to capture image.")
            break

        cv2.imshow("Capture Image", frame)

        # Wait for key press
        key = cv2.waitKey(1)
        if key == 27:  # Esc key to exit
            break
        elif key == 32:  # Space key to capture
            image_path = "captured_image.jpg"
            cv2.imwrite(image_path, frame)
            image_path_var.set(image_path)
            messagebox.showinfo("Info", f"Image saved as {image_path}.")
            break

    cap.release()
    cv2.destroyAllWindows()

def process_image():
    """Process the captured image."""
    image_path = image_path_var.get()
    if not image_path:
        messagebox.showwarning("Warning", "Please capture an image first.")
        return


    # Get selected language
    language_code = language_var.get()
    if language_code == "Telugu":
        language_code = "te"
    elif language_code == "Hindi":
        language_code = "hi"
    else:
        language_code = "en"

    # Generate and display the description
    description = describe_scene(image_path, language_code)
    description_var.set(description)

# Create the main window
root = tk.Tk()
root.title("Blind Assistance AI")

# Image capture
tk.Label(root, text="Capture an Image:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
image_path_var = tk.StringVar()
tk.Button(root, text="Capture", command=capture_image).grid(row=0, column=1, padx=10, pady=10)

# Language selection
tk.Label(root, text="Select Language:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
language_var = tk.StringVar(value="English")
tk.OptionMenu(root, language_var, "English", "Telugu", "Hindi").grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Process button
tk.Button(root, text="Process Image", command=process_image).grid(row=2, column=1, padx=10, pady=20)

# Description output
tk.Label(root, text="Scene Description:").grid(row=3, column=0, padx=10, pady=10, sticky="nw")
description_var = tk.StringVar()
tk.Label(root, textvariable=description_var, wraplength=400, justify="left").grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Run the application
root.mainloop()
