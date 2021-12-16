import cv2 as cv
import numpy as np

photo = cv.imread("papagan.jpg")
cv.imshow("Orjinal Image", photo)
#cv.waitKey()
blue = photo[:, :, 0]
green = photo[:, :, 1]
red = photo[:,:,2]
cv.imshow("Blue Band" , blue)
cv.imshow("Green Band" , green)
cv.imshow("Red Band" , red)
cv.waitKey()
#First way to make gray
photoGray = cv.imread("papagan.jpg", 0);
cv.imshow("GrayPhoto" , photoGray)
cv.waitKey()
#Second way to make gray with math
from matplotlib import pyplot as plt

imgGray = blue * 0.1140 + green * 0.5870 + red * 0.2889;
plt.imshow(imgGray, cmap='gray')
plt.show()

cv.waitKey()

