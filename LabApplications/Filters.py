import cv2 as cv
import numpy as np

image = cv.imread("../Resources/Lenna.png")
#Bir görüntünün parlaklık değerini nasıl buluruz ?
#Cevap ==> Tüm piksellerin yoğunluk değerlerini toplarız ve piksel sayısına böleriz .

#Average Filter (Ortalama filtre)
#Ortalama filtre 3 x 3 lük bir pencere al görüntüye oturt ve bir piksel bir piksel kaydırarak
# devam ettir. Bu 3 x 3 lük pencereye biz kernel deriz.
# bu bencere ye denk gelen pikseller kernelin değerleri ile çarpılır ve toplanır biz bu işleme
#Konvülsiyon deriz . Konvulsiyon ile elde ettiğimiz değeri yeni görüntü de (filtrelenmiş görüntü de )
# orjinal görüntüde kernelin merkezinin denk geldiği kordinatın değerlerinin hedef alındğı yere yerleştirirz
blur_filter1 = np.ones((3,3),np.float64)/(9.0)
blur_filter2 = np.ones((8,8),np.float64)/(64.0)
blur_filter3 = np.ones((12,12),np.float64)/(144.0)

#kernel büyüdükçe beyazlaşması daha parlak bir görüntü elde etmemizin sebebi
#12 12 de 144 pikseli toplayıp 12'ye bölüyoruz böylece yüksek sayılar çıkıyor ama
#3 3 de 9 sayıyı(pikseli) toplayıp 9'a bölüyoruz o yüzden daha yeterli bir blurlu seviye geliyor .

#cv filter2D metodu neyi neyle verirsen onu onla filtreler (Önemli Sınavda sorabilir.)
image_blur1 = cv.filter2D(image,-1,blur_filter1)
image_blur2 = cv.filter2D(image,-1,blur_filter2)
image_blur3 = cv.filter2D(image,-1,blur_filter3)

cv.imshow("Original Lena",image)
cv.imshow("Blur1 Lena",image_blur1)
cv.imshow("Blur2 Lena",image_blur2)
cv.imshow("Blur3 Lena",image_blur3)
cv.waitKey()

