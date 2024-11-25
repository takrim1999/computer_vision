import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
# print(capture.read()[1])
while True:
    Frame = capture.read()[1]
    # Drawing BD FLag
    # Frame = cv.rectangle(Frame,((Frame.shape[0]//2)-30,(Frame.shape[1]//2)-20),(Frame.shape[0]//2+30,Frame.shape[1]//2+20),[15,255,15],-1)
    # Frame = cv.circle(Frame,(Frame.shape[0]//2,Frame.shape[1]//2),15,[0,0,255],-1)
    cv.imshow("Video",Frame)
    if cv.waitKey(20) and (0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()