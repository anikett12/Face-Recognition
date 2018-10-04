# Face-Recognition
Face Recognition : live face recognition using Python and OpenCV 
## DataBase
Database has been created using SQLite studio.
[here](https://sqlitestudio.pl/index.rvt?act=download) is the link to download SQLite studio.

## Components
The project can be divided into three major subparts.

### creating dataset
The face of the person is detected using [haarscascade classifier](https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html).
An image is stored in a particular format i.e.  **user.userid.imagenumber** .

Images are aligned together one after the other.

example: ![user 1 3](https://user-images.githubusercontent.com/35431962/46495322-bb3c2080-c832-11e8-9953-57478ea9779c.jpg) ![user 1 1](https://user-images.githubusercontent.com/35431962/46497648-cc882b80-c838-11e8-9f8c-f19ece658f98.jpg) ![user 1 2](https://user-images.githubusercontent.com/35431962/46497671-dd38a180-c838-11e8-8db9-92ecfd71f4e9.jpg)

## training
Training is done using **LBPH face recognizer**.
To know more about it click [here](https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b) .

## Identification
First the face is detected and then LBPH recognizer is used to identify the detected face.
