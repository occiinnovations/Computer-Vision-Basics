import cv2
import numpy as np

metime = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not metime.isOpened():
    print("Camera index 0 failed. Trying index 1... 🛠️")
    metime = cv2.VideoCapture(1, cv2.CAP_DSHOW)

print("Feed active. Press 'q' to kill the window. ⚰️")

while True:
    ret, frame = metime.read()
    
    if not ret:
        print("Dropped frame. USB cable feeling loose? 🔌")
        break


    cv2.imshow('Pure Feed - No Math Allowed', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

metime.release()
cv2.destroyAllWindows()