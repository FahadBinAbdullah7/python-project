import cv2

img=cv2.imread("download (1).jpg")

grayImg= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresImg = cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)[1]


cv2.imwrite("gTHRESHOLDIMG.jpg",thresImg)
 
