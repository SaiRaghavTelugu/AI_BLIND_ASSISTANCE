from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from translation_tts_module import translate_text, speak_text
import os

# Force CPU
device = torch.device("cpu")

# Load BLIP base model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=True)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

def format_description(scene_text, detected_objects, recognized_text=""):
    """Generate structured scene description."""
    description = f"Scene shows {scene_text}."

    if detected_objects:
        formatted_objects = ", ".join(detected_objects)
        description += f" Detected objects: {formatted_objects}."

    if recognized_text:
        description += f" Recognized text: '{recognized_text}'."

    return description

def describe_scene(image_path, detected_objects=None, language_code='en'):
    """Generate scene description, translate to the selected language, and speak."""
    print("Starting scene description...")  # Debug print

    if not os.path.exists(image_path):
        print(f"Error: Image '{image_path}' not found.")
        return "Image not found."

    try:
        image = Image.open(image_path).convert("RGB")
        image = image.resize((384, 384))  # Resize image to reduce memory
        inputs = processor(images=image, return_tensors="pt").to(device)
        output = model.generate(**inputs)
        scene_text = processor.batch_decode(output, skip_special_tokens=True)[0]
        print(f"Scene description in English: {scene_text}")  # Debug print
    except Exception as e:
        print(f"Scene description error: {e}")
        scene_text = "A generic scene"

    # Step 1: First create in English
    english_description = format_description(scene_text, detected_objects or [], recognized_text="")

    # Debug print to check if description was created correctly
    print(f"Formatted Description (English): {english_description}")

    # Step 2: Translate entire description to the chosen language
    try:
        translated_description = translate_text(english_description, target_language=language_code)
        print(f"Translated Description: {translated_description}")  # Debug print
    except Exception as e:
        print(f"Translation error: {e}")
        translated_description = "Translation error."

    # Step 3: Save translated description to file
    with open("scene_description.txt", "w", encoding='utf-8') as file:
        file.write(translated_description)

    # Step 4: Speak the translated description
    print("Speaking:", translated_description)
    speak_text(translated_description, language=language_code)

    return translated_description