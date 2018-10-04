import os
import cv2
import numpy as np
from PIL import Image
recognizer=cv2.face.LBPHFaceRecognizer_create();
path='C:\\Users\\Aniket\\PycharmProjects\\Face Recognition sqlite\\DataSet'
def getImagesWithId(path):
    imagepaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagepath in imagepaths:
        faceImg=Image.open(imagepath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagepath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10);
    return np.array(IDs),faces
IDs,faces=getImagesWithId(path)
recognizer.train(faces,IDs)
recognizer.save('C:\\Users\\Aniket\\PycharmProjects\\Face Recognition sqlite\\recognizer\\trainingdata.yml')
cv2.destroyAllWindows()
