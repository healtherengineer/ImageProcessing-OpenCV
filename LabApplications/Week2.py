import cv2 as cv
import numpy as np

foto = cv.imread("indir.jpg")
# gray_foto = cv.imread("indir.jpg",0)
# cv.imshow("GrayBaboon",gray_foto)
# cv.imshow("Baboon", foto)
# cv.waitKey()

# B = foto[:, :, 0];
# G = foto[:, :, 1];
R = foto[:, :, 2];
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
# cv.imshow("Blue", B)
# cv.imshow("Green", G)
# cv.imshow("Red", R)

print(foto.shape)
#foto.shape = satır , sütün , bant.

print(R.shape)
# x = 1
# y = 1
# dimension = 0
# yogunluk_rgb = foto[y, x,dimension]
# yogunluk_r = R[y, x]
# print("Yogunluk : " + str(yogunluk_rgb))
# print("R'nin yoğunluğu : " + str(yogunluk_r))

# cv.waitKey()

# How to make gray with cv
# fotogray = cv.imread("indir.jpg" , 0)
# cv.imshow("Baboongray" ,fotogray)
# cv.waitKey()

# how to make gray with matplotlib
from matplotlib import pyplot as plt

# imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
# plt.imshow(imgGray , cmap='gray') #cmap 'gray' fonksiyonun adı
# plt.show()
# cv.waitKey()


renkli = cv.imread("indir.jpg")
gri = cv.imread("indir.jpg", 0)
cv.imshow("Baboon", renkli)
cv.imshow("GrayBaboon", gri)

# # Calcualte Histogram
# hist_color = cv.calcHist([renkli], [0], None, [256], [0, 256])
# hist_gray = cv.calcHist([gri], [0], None, [256], [0, 256])
#
# plt.figure("Renkli Figure Histogram")
# plt.plot(hist_color)
# plt.figure("Gray Figure Histogram")
# plt.plot(hist_gray)
#
# B = renkli[:,:,0]
# histogramOfBlueBand = cv.calcHist([B],[0],None,[256],[0,256])
# print(np.sum(histogramOfBlueBand))
# plt.figure("Histogram Of Blue Band")
# plt.plot(histogramOfBlueBand)
# plt.show()
plt.figure("Michelson Katsayısı")
CM = (np.max(gri) - np.min(gri))/(np.max(gri) + np.min(gri))
yeni = CM*gri
plt.imshow(yeni , cmap='gray') #cmap = colormap
plt.show()

