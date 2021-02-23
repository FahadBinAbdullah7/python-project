import cv2

img=cv2.imread("download (1).jpg")

gaussianBlurImg= cv2.GaussianBlur(img, (21,21),0)

cv2.imwrite("gaussianblurimg.jpg",gaussianBlurImg)
