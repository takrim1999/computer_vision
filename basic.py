import cv2 as cv
image = cv.imread('Resources/Photos/park.jpg')
cv.imshow('main',image)
# image = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
image = cv.GaussianBlur(image,(9,9),2)
# cv.imshow('main',image)
image = cv.Canny(image,100,120)
title = "Canny Edge"
cv.imshow(title, image)
cv.waitKey(0)