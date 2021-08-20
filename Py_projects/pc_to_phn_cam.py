import cv2
import numpy as np
url = 'http://192.168.1.11:8080/video'
cap = cv2.VideoCapture(url)
print(cap)
while(True):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame',frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()