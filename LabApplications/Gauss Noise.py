import cv2 as cv
import numpy as np
from skimage.util import random_noise

image = cv.imread("../Resources/Lenna.png")
image1 = cv.imread("../Resources/nike-apple.png")
# Gürültü 0 ve 255 den oluşan bozuk piksel değerlerinden oluşan görüntü


#s = np.random.normal(mu, sigma, 1000)
#mu, sigma = 0, 0.1 # mean and standard deviation
gauss = np.random.normal(0, 1, image.size)
# gauss gürültüsü için image size boyutunda bir vektör olışturduk
#gauss fonksiyonu oluşturduk aslında


gauss = gauss.reshape(image.shape[0], image.shape[1], image.shape[2]).astype('uint8')
# bu vektörü 3 bantlı bir matris haline getirdik

img_gauss = cv.add(image, gauss)

gaussian_blur = cv.GaussianBlur(img_gauss, (3, 3), 0)
blur_filter1 = np.ones((3, 3), np.float64) / (9.0)
ortalama_filter = cv.filter2D(img_gauss, -1, blur_filter1)
median_filter = cv.medianBlur(img_gauss, 3)
cv.imshow("Orijinal goruntu", image)
cv.imshow("Gauss Gurultusu", gauss)
cv.imshow("Gauss gurultulu Resim", img_gauss)
cv.imshow("Ortalama filtre uygulanmış gauss", ortalama_filter)
cv.imshow("Gauss ile iyilestirilmis goruntu ", gaussian_blur)
cv.imshow("Median filter ile iyilestirilmis goruntu", median_filter)
cv.waitKey()

# Random gürültü ekleme fonksiyonu
noise_image = random_noise(image1, mode='s&p', amount=0.1)
noise_image = np.array(255 * noise_image, dtype='uint8')
img_gaussian = cv.GaussianBlur(noise_image, (3, 3), 0)
img_bilateral = cv.bilateralFilter(noise_image, 3, 70, 50)
img_median = cv.medianBlur(noise_image, 3)
blur_filter1 = np.ones((3, 3), np.float64) / (9.0)
average_image = cv.filter2D(noise_image, -1, blur_filter1)
# Sonuclar
cv.imshow("Orijinal goruntu", image1)
cv.imshow("Random gurultulu", noise_image)
cv.imshow("Gauss ile iyileştirilmiş Resim", img_gaussian)
cv.imshow("Ortalama filtre uygulanmış Resim", average_image)
cv.imshow("Bilateral uygulanmis ", img_bilateral)
cv.imshow("Median filter ile iyilestirilmis goruntu", img_median)
cv.waitKey()
