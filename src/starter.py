import cv2
import numpy as np

libs = ["Mediapipe", "YOLOv8", "PyTorch", "PyTesseract"]

choices = []

for choice in libs:
    print(f"Apply {choice} to OpenCV?")
    y_n = input("Yes or No: ")

    if y_n == "Yes" or y_n == "yes":
        choices.append(choice)
    elif y_n == "No" or y_n == "No":
        pass
    else:
        print("Error, please enter yes or no")
        y_n == input("Yes or No: ")
        if y_n == "Yes" or y_n == "yes":
            choices.append(choice)

print(f"You chose {choices}.")

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
