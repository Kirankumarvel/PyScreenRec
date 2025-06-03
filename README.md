
# 🎥 PyScreenRec

**PyScreenRec** is a simple and lightweight screen recorder built with Python. It captures your screen in real-time and saves it as an MP4 video file. Ideal for coding tutorials, walkthroughs, or debugging sessions.

---

## 🚀 Features

* ✅ Full-screen recording in real-time
* ✅ Output in `.mp4` format using XVID codec
* ✅ Press **'q'** anytime to stop recording
* ✅ Beginner-friendly and minimal setup

---

## 🛠 Installation

First, install the required dependencies:

```bash
pip install opencv-python pyautogui numpy keyboard
```

> ⚠️ If you're using Python 3 and `pip` points to Python 2, use `pip3` instead.

If you're having issues with `pyautogui`, run:

```bash
python -m pip install pyautogui
```

---

## 💻 How to Use

1. Save the script as `PyScreenRec.py`.
2. Run it from the terminal or PowerShell:

```bash
python PyScreenRec.py
```

3. You'll see:

```
Recording... Press 'q' to stop.
```

4. Press **q** to stop recording.
5. The video is saved as `screen_recording.mp4` in your current folder.

---

## 🧠 Behind the Scenes

```python
import cv2
import numpy as np
import pyautogui
import keyboard

screen_size = pyautogui.size()
fps = 20
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_file = "screen_recording.mp4"
out = cv2.VideoWriter(output_file, fourcc, fps, (screen_size.width, screen_size.height))

print("Recording... Press 'q' to stop.")

while True:
    screen = pyautogui.screenshot()
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)
    
    if keyboard.is_pressed('q'):
        print("Recording stopped.")
        break

out.release()
print(f"Video saved to {output_file}")
```

---

## ❗ Troubleshooting

* **ModuleNotFoundError: No module named 'pyautogui'**

  * Run: `pip install pyautogui`
* **Keyboard input doesn't stop recording?**

  * Ensure the terminal window is in focus while pressing **q**.
  * Try running with admin rights if needed on Windows.
* **Screen recording lag?**

  * Lower the `fps` value in the script (e.g., from 20 to 10).

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

---

