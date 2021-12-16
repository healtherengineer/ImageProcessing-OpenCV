import cv2 as cv
import numpy as np
origin = cv.imread("../Resources/UEFA.png")
image = cv.cvtColor(origin,cv.COLOR_BGR2GRAY)
#threshold(img , sınır , değer , function)

ret  , thres1 = cv.threshold(image , 80,255,cv.THRESH_BINARY)
ret1 , thres2 = cv.threshold(image , 852,255,cv.THRESH_BINARY_INV)
ret2 , thres3 = cv.threshold(image , 120,255,cv.THRESH_TRUNC)
ret3 , thres4 = cv.threshold(image , 200,255,cv.THRESH_TOZERO)
ret4 , thres5 = cv.threshold(image , 120,255,cv.THRESH_TOZERO_INV)
cv.imshow("Original" , origin)
cv.imshow("Gray Image", image)
cv.imshow("Binary Threshold" , thres1)
cv.imshow("Binary Invert" , thres2)
cv.imshow("Turncated Threshold", thres3)
cv.imshow("Set to 0 " , thres4)
cv.imshow("Set to 0 Inverted" , thres5)
#belirli aralıklar arası eşiklemee
#Daha esnek bir thresholding fonksiyonudur.
#yoğunluk değerleri 10 ile 70 arasında olanları 255 yap gerisini 0 la
myResult = cv.inRange(image,10,70)
cv.imshow("Aralikli", myResult)
cv.waitKey()

