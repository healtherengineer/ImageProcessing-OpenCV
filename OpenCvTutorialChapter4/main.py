import cv2 as cv
import numpy as np

# How to create an Image
img = np.zeros((512, 512, 3), np.uint8)
# img[:] = 255,0,0  Blue All
# Let's create an blue box in the middle of the picture
# img[100:200 ,250:512] = 0,0,255

cv.line(img, (0, 0), (img.shape[1], img.shape[0]), (201, 237, 154), 2)
# Aqua btw, (width,height) (column ,row) thickness = kalınlık
cv.rectangle(img, (0, 0), (350, 250), (0, 0, 255), 3)
# cv.FILLED fills inside of the rectangle
cv.circle(img, (350, 400), 30, (255, 255, 255), 3)
# at the center there is a big circle :)
cv.circle(img, (int((img.shape[1] / 2)), int((img.shape[0] / 2))), int(img.shape[1] / 2), (255, 255, 255), 3)
cv.putText(img, " EGE BARISAN ", (int(img.shape[1] / 2 - (200)), 300), cv.FONT_ITALIC, 0.8, (20, 148, 20), 1)
cv.imshow("Image", img)
cv.waitKey(0)
