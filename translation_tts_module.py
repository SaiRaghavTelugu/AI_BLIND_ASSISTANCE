from deep_translator import GoogleTranslator
from gtts import gTTS
import os

def translate_text(text, target_language='te'):
    """Translate text to the target language."""
    try:
        return GoogleTranslator(source='auto', target=target_language).translate(text)
    except Exception:
        return text  # Return original text in case of error

def speak_text(text, language='en'):
    """Convert text to speech using gTTS."""
    try:
        tts = gTTS(text=text, lang=language)
        tts.save("output.mp3")
        os.system("start output.mp3")  # For Windows
    except Exception:
        pass  # Silently ignore TTS errors

def process_translated_objects(objects, language_code='te'):
    """Translate detected objects and speak them out loud."""
    try:
        translated_objects = [translate_text(obj, target_language=language_code) for obj in objects]
        translated_text = ', '.join(translated_objects)
        speak_text(translated_text, language=language_code)
        return translated_objects
    except Exception:
        return []