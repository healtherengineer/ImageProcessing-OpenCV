import cv2 as cv
import numpy as np

img = cv.imread("../Resources/nike-threshold.jpg")
img = cv.resize(img, (500, 400))
image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Hazır Fonksiyon ile bir resmin tersini alma
inverted = np.invert(image)

# canny_image = cv.Canny(image , 150,100)
# cv.imshow("Canny Image" , canny_image)

# Tüm resmi 255 ile farkını alarak Tersini alma
# Ya da en yüksek yoğunluk değeri ile farkını alarak Tersini alabilirdik
# fakat genelde 255 olacağından 255 ile almak daha sağlıklı
negative_image = np.max(image) - image  # 255 - image da yazabilirdik aynı şey .
# you did your homework
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        image[y][x] = 255 - image[y][x]

cv.imshow("Original Image", img)
cv.imshow("Inverted Image with for", image)
cv.imshow("Inverted with equation", negative_image)
cv.imshow("Inverted with function", inverted)
cv.waitKey()
