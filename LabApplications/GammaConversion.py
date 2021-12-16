import cv2 as cv
import numpy as np

image = cv.imread("../Resources/fenerbahce.jpg")
image = cv.resize(image , (500,500))
cv.imshow("Original" , image)
#gamma formül == s*r^y (s = sabit , r  = görüntü , y =gamma değeri)
#Gamma değeri 1 ise girdi ne ise çıktı da o olur
#Açıklama :
#image/255 yapmak  0 ile 1 arasında bir sayı elde etmektir
#0 ile 1 arasında bir sayının 1 den büyük bir üssünü alırsak sayı küçülür (bir basamak kayar hatta)
#255 ile çarpmamız 0.1 tabanli bir sayıyı 2 tane onluk tabanla büyütürken
#0.001 sayısında ise bir basamaklı yapar
# 0.1 * 255 = 25.5
#0.001 *255 = 2.55 !! :)
for gamma in [1,0.1,0.5,1.2,2.2,4,10]:
    gamma_corrected = np.array(255 * ((image/255) ** gamma),dtype='uint8')
    cv.imshow("Gamma Conversion "+ str(gamma), gamma_corrected)
    cv.waitKey()

#Bir görüntünün parlaklığını bulmak için
#Görüntüdeki tum yoğunluklar toplanıp piksel sayısına bölünür .

