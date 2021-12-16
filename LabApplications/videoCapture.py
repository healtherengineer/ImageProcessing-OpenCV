import  cv2 as cv
import numpy as np

screenRead = cv.VideoCapture(0)

while(1):
    _, image = screenRead.read()
    #iki değer döndüğü için alt tire koyduk
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret,esik_image = cv.threshold(gray , 150,255,cv.THRESH_BINARY)
    kernel = np.ones((5,5) , np.uint8)
    erosion = cv.erode(esik_image,kernel,iterations=3)
    #eşiklenen görüntü üstünde erode yapıyoruz
    cv.imshow("Video with erode" , erosion)
    cv.imshow("Original Video ", esik_image)
    if cv.waitKey(1) & 0xFF == ord('a'):
        break