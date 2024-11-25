import numpy as np
import cv2 as cv

blank = np.zeros((500,500,3),dtype='uint8')

cv.imshow('Dark Image',blank)
# green_square = blank[:,:,:]
# green_square[250:300,250:300] = 0,255,0
# cv.imshow('green pic',green_square)
squared_image = cv.rectangle(blank,(50,50),(300,300),(255,255,0),thickness=2)
squared_image = cv.putText(squared_image,"ADMIN",(25,300+70),5,5,(255,0,255))
cv.imshow('squared Image',squared_image)
cv.waitKey(0)