import cv2

img = cv2.imread ("download (1).jpg")

grayImg= cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayImage.jpg",grayImg)
cv2.imshow ("Original.jpg",img)
cv2.imshow ("GrayImage.jpg",grayImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
