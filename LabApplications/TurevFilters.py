import cv2 as cv
import numpy as np

image = cv.imread("../Resources/einstein.jpg", 0)

#Prewitt türev filtreleri
x_filter = np.array([[-1, -1, -1], [0, 0, 0], [1,1,1]])
y_filter = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

image_x = cv.filter2D(image,-1, x_filter)
image_y = cv.filter2D(image,-1,y_filter)

#Laplace (2.Türev) filtreleri.
laplace = cv.Laplacian(image, cv.CV_16S,ksize=5)
laplace2 = cv.Laplacian(image , cv.CV_32F)

#Results
cv.imshow("Original " , image)
cv.imshow("Yatay yon", image_x)
cv.imshow("Dikey yon" , image_y)
cv.imshow("Laplace", laplace)
cv.imshow("Laplace 2" , laplace2)
cv.waitKey(0)

