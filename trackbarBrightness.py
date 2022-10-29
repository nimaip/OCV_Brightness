import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def empty(a):
    pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Brightness", "TrackBars", 0, 510, empty)

while True:
    b = cv2.getTrackbarPos("Brightness", "TrackBars")
    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    under = False

    if b > 255:
        b -= 255
        under = True

    M = np.ones(img.shape, dtype="uint8") * b
    if under:
        added = cv2.add(img, M)
    else:
        added = cv2.subtract(img, 255-M)
    cv2.imshow("Brightness Changing", added)

    cv2.waitKey(1)