import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = cv.imread("indir.jpg", 0)

#Resmi iyileştirmek için blurladık
image = cv.medianBlur(image, 5)

ret, th1 = cv.threshold(image, 90, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 2)
#(3,2) lik bir matrisle geziniyor matrisi
th3 = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 3, 2)
titles = ["Original Image", "Global Thresholding(v = 90)", "Adaptive average thresholding",
          "Adaptive Gausian Thresholding"]
images = [image, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, (i + 1)), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

cv.waitKey()
