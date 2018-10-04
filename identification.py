import cv2
import numpy as np
import sqlite3
FaceDetect=cv2.CascadeClassifier('C:\\Users\\Aniket\\PycharmProjects\\facedetection\\haarcascade_frontalface_default.xml');
true =FaceDetect.load('C:\\Users\\Aniket\\PycharmProjects\\facedetection\\haarcascade_frontalface_default.xml')

def getProfile(id):
    con=sqlite3.connect("facedatabase1.db")
    cmd="SELECT * FROM people WHERE ID="+ str(id)
    cursor=con.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    con.close()
    return profile

cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read('C:\\Users\\Aniket\\PycharmProjects\\Face Recognition sqlite\\recognizer\\trainingdata.yml')
id=0
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=FaceDetect.detectMultiScale(gray,1.3,5);
    font=cv2.FONT_HERSHEY_SIMPLEX
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getProfile(id)
        if(profile!=None):
            cv2.putText(img,profile[1],(x,y+h+30),font,1,(0,0,150))
            cv2.putText(img,profile[2],(x,y+h+70),font,1,(0,0,150))
            cv2.putText(img,profile[3],(x,y+h+110),font,1,(0,0,150))
            
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
