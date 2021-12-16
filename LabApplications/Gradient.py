import cv2 as cv
import numpy as np

image = cv.imread("../Resources/yildiz.jpg")

cv.imshow("Original Space image", image)


kernel = np.ones((2,2) ,dtype=np.uint8)
gradient_image = cv.morphologyEx(image , cv.MORPH_GRADIENT,kernel)
cv.imshow("Gradient Image" ,gradient_image)
#We use gradient to find edges of shapes inside the image
# genisleme = cv2.dilate(img,kernel,iterations=1)
# erozyon = cv2.erode(img,kernel,iterations=1)
# fark = genisleme-erozyon

cv.waitKey()

