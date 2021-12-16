import cv2 as cv
import numpy as np

image = cv.imread("../Resources/einstein.jpg")
#Buyük bir alanda daha fazla fark olur
#o yüzden kernel in size ı büyükçe daha çok bulanık oluyor
#düz bir kenar çizgisini düşün
#Keskinlik Resmin içindeki yoğunluk değelerinin farkının fazlalaşmasıdır .(Belirginlik)
gaussian_blur = cv.GaussianBlur(image,(5,5),0) #kenar bölegeye etkisini gideriyor



#Median blur  = hepsini alır sıralar sonra orta değer bulur merkez piksele koyar
# yana kayar böyle böyle görüntüyü blurlar. eğer kernel size'ı büyürse ortanca değer çok farklı geleceğinden daha çok
#bulanıklaşır.
#kernel size'ı asla çift değer veremezsin(çift sayı verirsen piksel sayısı çift gelir çiftin ortası yoktur)
# genelde 3 x 3 olur
median_blur = cv.medianBlur(image,3)

cv.imshow("Median Blur",median_blur)
cv.imshow("Original" , image)
cv.imshow("Gaussian Blur", gaussian_blur)
cv.waitKey()