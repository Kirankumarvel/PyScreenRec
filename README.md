# 🎥 PyScreenRec

**PyScreenRec** is a simple, modular Python-based screen recording suite with support for GUI, webcam, and audio capture. Designed for developers, content creators, and educators who want lightweight screen recording tools built with pure Python.

---

## 📁 Project Structure

```bash
PyScreenRec/
├── requirements.txt                    # Base requirements (for CLI version)
├── PyScreenRec_GUI/                   # GUI version using PyQt5
│   ├── PyScreenRec_GUI.py
│   └── requirements.txt
├── PyScreenRec_WebCam_Audio/         # Webcam + audio version (CLI)
│   ├── PyScreenRec_WebCam_Audio.py
│   └── requirements.txt
```

---

## 💡 Features

* ✅ Fullscreen screen recording
* ✅ Simple CLI version (base)
* ✅ GUI version using PyQt5
* ✅ Webcam + Audio capture version
* ✅ Lightweight and beginner-friendly
* ✅ Customizable and open-source

---

## 📦 Setup Instructions

### 🔹 Option 1: Base CLI Screen Recorder

```bash
pip install -r requirements.txt
python PyScreenRec.py
```

> 📌 Press `q` to stop recording.

---

### 🔹 Option 2: GUI Version

```bash
cd PyScreenRec_GUI
pip install -r requirements.txt
python PyScreenRec_GUI.py
```

> GUI lets you start/stop with buttons instead of hotkeys.

---

### 🔹 Option 3: Webcam + Audio Recording

```bash
cd PyScreenRec_WebCam_Audio
pip install -r requirements.txt
python PyScreenRec_WebCam_Audio.py
```

> 📌 Captures screen + microphone audio + webcam (optional webcam code can be added).

---

## ⚙️ Tech Stack

* Python 3.x
* `opencv-python`
* `pyautogui`
* `numpy`
* `keyboard`
* `sounddevice`, `soundfile` (for audio)
* `PyQt5` (for GUI)

---

## 📌 Notes

* For webcam overlay or audio-video merging into one file, additional tools like `ffmpeg` or `moviepy` may be used.
* Make sure Python and Pip are added to your system PATH.
* If you face any `ModuleNotFoundError`, ensure you're installing in the correct Python environment.

---

## 🧪 Coming Soon

* [ ] Audio + webcam merging into single `.mp4`
* [ ] In-app recording preview
* [ ] Export formats and resolution control

---

## 📃 License

MIT License – free to use, modify, and distribute.

---

