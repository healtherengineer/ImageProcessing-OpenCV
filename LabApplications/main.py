import cv2 as cv
import numpy as np

foto = cv.imread("indir.jpg")
cv.imshow("Baboon", foto)
#cv.waitKey()

B = foto[:,:, 0];
G = foto[:,:, 1];
R = foto[:,:, 2];
"""""
B = B *0;
B = B+255;
b1 = B;
b2 = B ;
B = B + b1 + b2 ;
normalGray = B *0.5 + b1 * 0.5870 + 0.1140 *b2;
cv.imshow("Normal Gray",normalGray)
print(B)

"""
cv.imshow("Blue", B)
cv.imshow("Green", G)
cv.imshow("Red", R)
cv.waitKey()

#How to make gray with cv
fotogray = cv.imread("indir.jpg" , 0)
cv.imshow("Baboongray" ,fotogray)
cv.waitKey()

# how to make gray with matplotlib
from matplotlib import pyplot as plt

imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(imgGray , cmap='gray') #cmap 'gray' fonksiyonun adı
plt.show()
cv.waitKey()
