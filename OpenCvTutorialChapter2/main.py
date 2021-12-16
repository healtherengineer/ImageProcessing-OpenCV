import cv2 as cv
import numpy as np
img = cv.imread("../Resources/Lenna.png")
#Let's create a matrix with filled ones using numpy
kernel = np.ones((5,5) , np.uint8)

imageGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imageGray,(7,7),0) #(7,7) kernel size
imgCanny = cv.Canny(img,150,100) # canny ımage accepts gray image in order to detection of edges
imgDialation = cv.dilate(imgCanny,kernel,iterations=1)  #We add same kernel such as the up
imgEroded = cv.erode(imgDialation ,kernel,iterations=1)
#imgEroded2 = cv.erode(imgCanny ,kernel,iterations=1)


cv.imshow("Gray Image", imageGray)
cv.imshow("Blur Image",imgBlur)
cv.imshow("Canny Image", imgCanny)
cv.imshow("Dialation Image", imgDialation)
cv.imshow("Eroded Image", imgEroded)
#cv.imshow("Eroded2 Image", imgEroded2)

cv.waitKey()