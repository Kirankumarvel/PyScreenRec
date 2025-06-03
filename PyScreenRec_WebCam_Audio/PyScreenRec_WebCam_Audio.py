import cv2
import numpy as np
import pyautogui
import sounddevice as sd
import soundfile as sf
import threading
import time

screen_size = pyautogui.size()
fps = 20
video_out = cv2.VideoWriter("combined_output.avi", cv2.VideoWriter_fourcc(*"XVID"), fps,
                            (screen_size.width, screen_size.height))
audio_filename = "audio.wav"
duration = 999  # seconds, will stop when screen ends

def record_audio():
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=2)
    sd.wait()
    sf.write(audio_filename, audio, 44100)

def record_screen():
    start = time.time()
    while time.time() - start < duration:
        screen = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
        video_out.write(frame)
        if cv2.waitKey(1) == ord('q'):
            break
    video_out.release()

# Run both in parallel
audio_thread = threading.Thread(target=record_audio)
video_thread = threading.Thread(target=record_screen)

print("Recording started. Press Ctrl+C to stop.")
audio_thread.start()
video_thread.start()
audio_thread.join()
video_thread.join()

print("Recording complete.")
