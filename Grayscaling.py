import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    captured, img = cap.read()
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.line(gray_image, (0,0), (480,500), (255,0,0), 5)
    cv.imshow("Live Broadcast", gray_image)
    if cv.waitKey(1) & 0xff == ord('e'):
        break

cap.release()
cv.destroyAllWindows()