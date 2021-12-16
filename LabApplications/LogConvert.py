import cv2 as cv
import numpy as np

#Logaritmic Conversion
image = cv.imread("indir.jpg",0)
cv.imshow("Original", image)

#Logaritmical Conversion da sabit bir sayı ile çarpıyoruz ve her pikselin logaritmasını alıyoruz
#c değeri büyüdükçe parlaklık artar

c=1
log_image = c*np.log(1+image)
log_image = np.array(log_image , dtype=np.uint8)
cv.imshow("Logaritmical Conversion" , log_image)

#daha sonra 255 i bu elde ettiğimiz logaritmik küçük değerlere bölerek daha aydınlık bir resim elde ediyoruz
log_image = 255/(c*np.log(1+image))
log_image = np.array(log_image , dtype=np.uint8)
cv.imshow("255 Conversion" , log_image)
cv.waitKey(0)