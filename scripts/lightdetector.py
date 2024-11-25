import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
# print(capture.read()[1])
while True:
    Frame = capture.read()[1]
    data = np.array(Frame).mean()
    # light_text = cv.putText(Frame,str(data),(0,50),cv.FONT_HERSHEY_TRIPLEX,2,[255,0,0],2)
    if data>100:
        cv.putText(Frame,"Light ON",(0,50),cv.FONT_HERSHEY_TRIPLEX,2,[0,255,0],2)
    elif (data>5) and data<=100:
        cv.putText(Frame,"Using Torch",(0,50),cv.FONT_HERSHEY_TRIPLEX,2,[255,0,0],2)
    else:
        cv.putText(Frame,"Light OFF",(0,50),cv.FONT_HERSHEY_TRIPLEX,2,[0,0,255],2)
    cv.imshow("Video",Frame)
    if cv.waitKey(20) and (0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()