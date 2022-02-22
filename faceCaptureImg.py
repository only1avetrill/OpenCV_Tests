import cv2 as cv

fase_cascade_db = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')

img = cv.imread('test.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = fase_cascade_db.detectMultiScale(img_gray, 1.1, 19)
for(x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('OpenCV test result', img)
cv.waitKey()