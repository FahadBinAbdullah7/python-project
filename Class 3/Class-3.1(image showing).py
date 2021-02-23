import cv2

img = cv2.imread ("download (1).jpg")

cv2.imshow ("download (1).jpg",img)
cv2.imwrite("download (1)Copy.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
