import pyttsx3
import os

def speak(text):
    """Converts text to speech."""
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Adjust speech rate
        engine.setProperty('volume', 1.0)  # Set volume to maximum
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {e}")

def speak_scene_description():
    """Reads 'scene_description.txt' and speaks the content."""
    if not os.path.exists("scene_description.txt"):
        print("Error: 'scene_description.txt' not found. No description to read.")
        return

    try:
        with open("scene_description.txt", "r",encoding="utf-8") as file:
            description = file.read().strip()
            if description:
                print(f"Speaking: {description}")
                speak(description)
            else:
                print("File is empty. Speaking fallback message.")
                speak("No scene description available.")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    print("Starting text-to-speech program...")
    speak_scene_description()
