import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#My Homework for this week
image = cv.imread("../Resources/Lenna.png",0)
cv.imshow("Lena",image)
cv.waitKey()
shape = image.shape #it is a tuple ,I mean it returns a tuple
r = shape[0]
c = shape[1]
histogramArray = np.zeros(256)

for y in range(0,r):
    for x in range(0,c):
        histogramArray[image[y][x]] +=1


plt.figure("My Histogram")
plt.xlabel("0-255 Color Values of Pixels")
plt.ylabel("Intensitive of the Points")
plt.plot(histogramArray)

realHistogram = cv.calcHist([image], [0], None, [256], [0, 256])#calcHist(image , , mask , histSize, histRange)
plt.figure("Real Histogram")
plt.xlabel("0-255 Color Values of Pixels")
plt.ylabel("Intensitive of the Points")
plt.plot(realHistogram)
plt.show()
#print(histogramArray)
