import cv2
import imutils
img=cv2.imread("download (1).jpg")
resizeImg=imutils.resize(img,width=4000)
cv2.imwrite("resizedImage.jpg",resizeImg)
