import cv2 as cv

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

def resizeFrame(frame,scale=0.5):
    newDimension =  (int(frame.shape[1]*scale),int(frame.shape[0]*scale))
    resizedFrame = cv.resize(frame,newDimension,interpolation=cv.INTER_AREA)
    return resizedFrame

while True:
    isTrue, Frame = capture.read()
    if not isTrue:
        break
    cv.imshow('Video',resizeFrame(Frame))
    if cv.waitKey(30) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()