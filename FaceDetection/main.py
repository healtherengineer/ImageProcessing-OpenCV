import cv2 as cv
import numpy as np

image = cv.imread("kids.jpg",0)
#image = cv.medianBlur(image , 3)
#kernel = np.ones((3,3))/9.0
#uygun gama değerini resme göre ayarlayabiliriz.
gamma = 2.2

image = np.array(255 * ((image/255) ** gamma),dtype='uint8')
#image = cv.filter2D(image, -1 , kernel)
#ret1,t_image = cv.threshold(image,80,255,cv.THRESH_BINARY)
# #gauss_img =  cv.medianBlur(image, 5)
# #ret,thresh1 = cv.threshold(image,5,255,cv.THRESH_BINARY)
# average_filter = np.ones((3,3) , np.uint8)/9.0
# #image = cv.filter2D(image,-1,average_filter)
# image =  cv.GaussianBlur(image ,(3,3), 0)
# ret1,t_image = cv.threshold(image,150,255,cv.THRESH_BINARY)
# kernel = np.ones((3,3))
#morpho_image = cv.dilate(t_image , kernel)
face_cascade =cv.CascadeClassifier("data/haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(image)
print("Görüntüde tespit edilen yüz sayısı : ", len(faces))

for x,y ,width , height in faces:
    cv.rectangle(image , (x,y) , (x+ width , y+height) , color=(255,255,255) , thickness=2)
    cv.imshow("Result" ,image)
cv.waitKey()

