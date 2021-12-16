import cv2 as cv
import numpy as np
from imageio import imread, imwrite

# Bu kodu hoca ile birlikte incele
#neden imwrite yapınca farklı imshow yapınca farklı
original = cv.imread("../Resources/eifellTower.jpg")
cv.imshow("Original Image", original)

image = imread("../Resources/eifellTower.jpg")

arr = image * np.array([0.1, 0.2, 0.5])
# astype ile bu hatayı ortadan kaldırırız
arr2 = (255 * arr / arr.max()).astype(np.uint8)
night_image1 = cv.imshow("Night 1 ", arr2)

imwrite("night.png", arr2)
img2 = cv.imread('night.png')

gamma = 2

gamma_img = np.array(255 * (img2 / 255) ** gamma)
night_image1 = cv.imshow("Night 2 ", gamma_img)

cv.imwrite("night_final.png", gamma_img)
cv.waitKey()
# Warning explantation:Lossy conversion from float64 to uint8
# Verdiği hata resimdeki bazı değerlerin float64 ve uint8 değerleri çarpılıyor ve değerler genel olarak yuvarlanıyor
# pek bir değişim olmaz ama pycharm bizi uyarıyor haberimiz olsun diye.
# astype ile bu uyarıyı ortadan kaldırırız
