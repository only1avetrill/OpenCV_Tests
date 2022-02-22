import cv2 as cv

fase_cascade_db = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')

capture_cam = cv.VideoCapture(0)

while True:
    success, img = capture_cam.read( )
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = fase_cascade_db.detectMultiScale(img_gray, 1.1, 19)
    for(x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow('OpenCV test result', img)
    if cv.waitKey(1) & 0xff == ord('q'):
        break
        capture_cam.release()
        cv.destroyAllWindows()

