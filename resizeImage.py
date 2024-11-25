import cv2 as cv

image = cv.imread('Resources/Photos/cat_large.jpg')

# cv.imshow('Large Cat',image)
# cv.waitKey(0)

# image = cv.resize(image,(int(image.shape[1]*0.75),int(image.shape[0]*0.75)),interpolation=cv.INTER_AREA)
# cv.imshow('Resized Image',image)

height = image.shape[0]
width = image.shape[1]

image = cv.resize(image,(800,400),interpolation=cv.INTER_AREA)
print(image.shape)
cv.imshow('Resized Image',image)
cv.waitKey(0)