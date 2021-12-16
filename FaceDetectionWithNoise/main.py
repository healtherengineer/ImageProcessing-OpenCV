import cv2 as cv
import numpy as np
from skimage.util import random_noise

image = cv.imread("kids.jpg", 0)

noise_image = random_noise(image, mode='s&p', amount=0.1)
noise_image = np.array(255 * noise_image, dtype='uint8')
image = noise_image
cv.imshow("Noise Image" , image)
cv.waitKey()
# Bu 1. yöntem
# gamma = 2
# image = np.array(255 * ((image/255) ** gamma),dtype='uint8')


# Buda 2. yöntem
kernel = np.ones((3, 3)) / 9.0
image = cv.medianBlur(image, 3)
cv.imshow("Median Image" , image)
cv.waitKey()
image = cv.GaussianBlur(image, (3, 3), 0)
cv.imshow("median + Gaus Image" , image)
cv.waitKey()
image = cv.filter2D(image, -1, kernel)
cv.imshow("Mean+G+median Image" , image)
cv.waitKey()
gamma = 2
image = np.array(255 * ((image / 255) ** gamma), dtype='uint8')
#image = cv.equalizeHist(image)
face_cascade = cv.CascadeClassifier("data/haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(image)
print("Görüntüde tespit edilen yüz sayısı : ", len(faces))

for x, y, width, height in faces:
    cv.rectangle(image, (x, y), (x + width, y + height), color=(255, 255, 0), thickness=2)
    cv.imshow("Result", image)
cv.waitKey()
