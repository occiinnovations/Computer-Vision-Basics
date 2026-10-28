import cv2
import numpy as np

print(f"OpenCV Version: {cv2.__version__}\nStarting OpenCV...")

metime = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not metime.isOpened():
    print("Camera did not open.")
    metime = cv2.VideoCapture(1, cv2.CAP_DSHOW)

print("OpenCV activated. Press 'q' to quit.")

while True:
    ret, frame = metime.read()

    if not ret:
        print("OpenCV failed to read frame.")
        break

    cv2.imshow('OpenCV Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Exiting OpenCV...")

metime.release()
cv2.destroyAllWindows()
