import cv2
import numpy as np
from playsound import playsound
cam = cv2.VideoCapture(0)
ret, first_frame = cam.read()
if not ret:
    print("Error: Unable to access the camera")
    cam.release()
    exit()
first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_frame = cv2.GaussianBlur(first_frame, (21, 21), 0)

while True:
    ret, frame = cam.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    delta_frame = cv2.absdiff(first_frame, gray_frame)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    white_pixel_count = np.sum(thresh_frame == 255)
    if white_pixel_count > 1000:
        playsound(r'C:\Users\ganes\Downloads\computer-beeps-232200.mp3')
    cv2.imshow('Motion Detection', frame)
    if cv2.waitKey(1) == 27:
        break
cam.release()
cv2.destroyAllWindows()
