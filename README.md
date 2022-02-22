# Tests with OpenCV Python library
This is the test code made with OpenCV Computer Vision library. This project does not have any purpose, it is only necessary for my own training in learning Python from scratch and testing the possibilities of computer vision and artificial intelligence. Over time, new tests will appear here. This repository is purely for history and progress tracking.

To install OpenCV library use `pip install opencv-python` in console and import it to project by `import cv2`.

## Human face recognition
Human face recognition was implemented both from the image and from the webcam. To implement this function, a [file with presets for recognition](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) is used, which available in the OpenCV library and on [it’s GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades) (pre-trained models based on neural networks). For the first two tests, I used a trained model for recognising the frontal image of a face in a photo, which allows head rotation up to 30 degrees.

### 1. faceCaptureImg.py
![Capturing face from image](https://user-images.githubusercontent.com/75385700/155219537-e5afcc95-697e-47b1-bf98-25ae745c33aa.png)

An image from a photo stock, where people are in comfortable poses and look directly at the camera, is processed without problems and faces are recognised without error.

### 2. faceCaptureWebcam.py
![Capturing face from webcam](https://user-images.githubusercontent.com/75385700/155219908-1b0e4c6b-c201-48a4-8565-9db17b73ddf4.png) ![Capturing face from webcam with mask](https://user-images.githubusercontent.com/75385700/155220800-ce2b5320-6ed2-4445-b058-4cdcde7e9bf2.png)

Of course, in order to correctly recognise the face, you need to choose the appropriate positions for yourself and the webcam. In most cases this is what happens. Unexpectedly, the system worked several times with a mask on my face, but this does not always happen correctly.
