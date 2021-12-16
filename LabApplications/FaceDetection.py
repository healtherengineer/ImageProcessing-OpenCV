import cv2 as cv
import numpy as np


image = cv.imread("../Resources/kids.jpg")
cv.imshow("Kids", image)
cv.waitKey()