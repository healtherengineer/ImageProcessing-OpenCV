import cv2 as cv
import numpy as np
from skimage.util import random_noise

image = cv.imread("../Resources/yildiz.jpg",0)

ret, esik_image = cv.threshold(image, 80, 255, cv.THRESH_BINARY)
noise_img = random_noise(esik_image , mode="s&p" ,  amount=0.1)
#eklenecek gürültü sayısı , eklenecek gürültü pixeli sayısı
#0.1 kadar gürültü ekle büyükçe daha bozuk bir gürültü olur
noise_img = np.array(255*noise_img, dtype="uint8")
cv.imshow("Gurultulu giris goruntusu",noise_img)

kernel = np.ones((2, 2), dtype=np.uint8)
kernel2 = np.ones((5, 5), dtype=np.uint8)

erode_result = cv.erode(esik_image, kernel, iterations=1)
dilate_result = cv.dilate(esik_image, kernel , iterations=1)
opening = cv.morphologyEx(noise_img.astype(np.float32),cv.MORPH_OPEN,kernel)
#Açılma da önce erozyon sonra dilation uygulanır
closing = cv.morphologyEx(noise_img.astype(np.float32),cv.MORPH_CLOSE,kernel2)
#Kapatmada önce dilation(genişleme) sonra erozyon olur .
#closing üstüne erozyon yaptır !!!! Bak bakalım neler olacak kernel boyutunu değiştir düzelt bakalım nolacak
new_image = cv.erode(closing,kernel2,iterations=5)
cv.imshow("Original Baby", image)
cv.imshow("Esiklenen Goruntu", esik_image)
cv.imshow("Erozyonlu Esikli Goruntu",erode_result)
cv.imshow("Dilation Uygulanmis" , dilate_result)
cv.imshow("Acilma Uygulanmis Resim" , opening)
cv.imshow("Kapanma Uygulanmis Resim" , closing)
cv.waitKey()
