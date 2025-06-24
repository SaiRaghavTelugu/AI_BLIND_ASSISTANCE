# 👁️‍🗨️ Blind Assistance AI

Welcome to **Blind Assistance AI**!  
This Python app helps visually impaired users by describing scenes in real-time using your webcam, translating the description into your chosen language, and reading it aloud.  
Accessible, simple, and powerful!

---

## ✨ Features

- 📸 **Real-time Image Capture:** Snap images directly from your webcam.
- 📝 **Scene Description:** Get natural language captions using the BLIP model.
- 🌐 **Language Translation:** Instantly translate descriptions to **English**, **Telugu**, or **Hindi**.
- 🔊 **Text-to-Speech:** Hear the translated description with a single click.
- 🖥️ **User-Friendly Interface:** Simple GUI built with Tkinter.

---

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/BLIND_ASSISTANCE_AI.git
   cd BLIND_ASSISTANCE_AI
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   python main_ui.py
   ```

---

## 🕹️ How to Use

1. **Click** `Capture` to take a real-time image using your webcam.
2. **Choose** your preferred language from the dropdown.
3. **Click** `Process Image` to generate, translate, and hear the scene description.
4. **Listen** as the app reads out the description for you!

---

## 🗂️ Project Structure

```
BLIND_ASSISTANCE_AI/
├── main_ui.py
├── scene_description.py
├── translation_tts_module.py
├── requirements.txt
├── README.md
├── .gitignore
```

---

## 🧰 Requirements

- Python 3.8+
- torch
- torchvision
- transformers
- pillow
- gtts
- deep-translator
- opencv-python
- tkinter (usually included with Python)

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 💡 Notes

- The BLIP model and other dependencies will download automatically on first run.
- Make sure your webcam is connected and accessible.
- On Windows, audio output uses the default player.

---

## 📜 License

This project is for educational and research purposes.

---

**Enjoy using Blind Assistance AI! If you like it, ⭐ star the repo and share your

