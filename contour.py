import cv2 as cv
import numpy as np
image = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Image',image)
image = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
ret,image = cv.threshold(image,125,255,cv.THRESH_BINARY)
cv.imshow('BinaryImage',image)
cont,hier = cv.findContours(image,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
blank = np.zeros(image.shape[:2])
cv.drawContours(blank,cont,-1, (255,0,255), 1)
cv.imshow('Blank Image',blank)

cv.waitKey(0)