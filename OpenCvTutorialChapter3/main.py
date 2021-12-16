import cv2 as cv
import numpy as np

# How to Resize an Image

image = cv.imread("../Resources/fenerbahce.jpg")

# Let's resize
image_resize = cv.resize(image, (400, 300))
# cv.resize(targetPicture , (width (columns), height(rows))
#When we work on a pıcture , we write image[width , height] , image[x(axix)(columns), y(ordinate)(rows)]

#Let's Crop
#in right here , we take from 100st row untill 180st row and our rows are equal to 80 , in the same way
#We take from 100st column untill the end(256st) and our columns are equal to 156 .
#Cropped Image's shape is (80,156,3)(row,column ,BGR)

image_cropped = image[100:180,100:256]
cv.imshow("Cropped Image", image_cropped)
cv.imshow("Resized Image", image_resize)
cv.imshow("Original Image", image)
# it read as (row,column,BGR)

print(image.shape)
print(image_resize.shape)
print(image_cropped.shape)
cv.waitKey()
