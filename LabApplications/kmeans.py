import cv2 as cv
import numpy as np

img = cv.imread("../Resources/eifellTower.jpg")
img = cv.cvtColor(img , cv.COLOR_BGR2RGB)
twoDimage = img.reshape((-1,3))
twoDimage = np.float32(twoDimage)
criteria = (cv.TERM_CRITERIA_EPS  +cv.TERM_CRITERIA_MAX_ITER , 10 , 1.0)
K = 2
attempts = 10
ret,label , center = cv.kmeans(twoDimage , K, None , criteria , attempts , cv.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
result_image = res.reshape((img.shape))
cv.imshow('orijinal' , img)
cv.imshow('k=2 image' , result_image)
cv.waitKey(0)