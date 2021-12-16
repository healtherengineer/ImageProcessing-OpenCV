import cv2 as cv

#img = cv.imread("../Resources/Lenna.png")
#img = cv.imread("Lenna.png")

#cv.imshow("Lenna",img)
#cv.waitKey()

cap = cv.VideoCapture(0)
cap.set(3,640)# 3 is a id for width
cap.set(4,480) # 4 is a id for height
cap.set(10,1000)# 10 is a id for bright

while True:
    success ,img = cap.read();
    cv.imshow("Video",img);
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break