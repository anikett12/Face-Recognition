import cv2
import numpy as np
import sqlite3
FaceDetect=cv2.CascadeClassifier('C:\\Users\\Aniket\\PycharmProjects\\facedetection\\haarcascade_frontalface_default.xml');
true =FaceDetect.load('C:\\Users\\Aniket\\PycharmProjects\\facedetection\\haarcascade_frontalface_default.xml')

cam=cv2.VideoCapture(0);

def UpdateorInput(Id,name):
    con=sqlite3.connect("facedatabase1.db")
    cmd="SELECT * FROM people WHERE ID="+str(Id)
    cursor=con.execute(cmd)
    t=0
    for row in cursor:
        t=1
    if (t==1):
        cmd="UPDATE people SET Name =" + str(name)+" WHERE ID="+str(Id)

    else:
        cmd="INSERT INTO people(ID,Name) Values("+str(Id)+","+str(name)+")"
    con.execute(cmd)
    con.commit()
    con.close()

id = input('enter your id')
NAme=input('enter your Name')
UpdateorInput(id,NAme)
sampleNum=0;
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=FaceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("C:\\Users\\Aniket\\PycharmProjects\\Face Recognition sqlite\\DataSet\\User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.waitKey(100);
    cv2.imshow("Face",img);
    cv2.waitKey(1);
    if(sampleNum>20):
        break;
cam.release()
cv2.destroyAllWindows()
