import sys
import cv2
import numpy as np
import pyautogui
import keyboard
import sounddevice as sd
import soundfile as sf
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class ScreenRecorder:
    def __init__(self):
        self.is_recording = False
        self.output_file = "screen_recording.mp4"
        self.screen_size = pyautogui.size()
        self.fps = 20
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.out = cv2.VideoWriter(self.output_file, self.fourcc, self.fps,
                                   (self.screen_size.width, self.screen_size.height))

    def start_recording(self):
        self.is_recording = True
        threading.Thread(target=self.record_screen).start()

    def stop_recording(self):
        self.is_recording = False

    def record_screen(self):
        print("Recording started...")
        while self.is_recording:
            screen = pyautogui.screenshot()
            frame = np.array(screen)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.out.write(frame)

        self.out.release()
        print(f"Screen recording saved as {self.output_file}")


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.recorder = ScreenRecorder()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyScreenRec')
        layout = QVBoxLayout()

        self.label = QLabel("🎥 PyScreenRec\nClick below to start or stop recording.")
        layout.addWidget(self.label)

        self.start_btn = QPushButton("Start Recording")
        self.start_btn.clicked.connect(self.start_recording)
        layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton("Stop Recording")
        self.stop_btn.clicked.connect(self.stop_recording)
        layout.addWidget(self.stop_btn)

        self.setLayout(layout)
        self.resize(300, 150)

    def start_recording(self):
        self.recorder.start_recording()
        self.label.setText("Recording...")

    def stop_recording(self):
        self.recorder.stop_recording()
        self.label.setText("Recording stopped and saved.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = App()
    gui.show()
    sys.exit(app.exec_())
