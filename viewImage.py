import cv2 as cv

image = cv.imread('Resources/Photos/cat.jpg')

cv.imshow("Cat", image)

cv.waitKey(0)
