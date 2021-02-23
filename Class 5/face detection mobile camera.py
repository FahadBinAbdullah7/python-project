import cv2
import numpy
import time

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

cam=cv2.VideoCapture(0)

address="https://192.168.0.100:8080/cam"
cam.open(address)


count = 1
while count <100:
    print (count)
    _,img=cam.read()
    grayImg= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face= haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        count+=1
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
