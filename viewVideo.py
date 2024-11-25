import cv2 as cv

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue , Frame = capture.read()
    if not isTrue:
        break
    cv.imshow('video',Frame)
    if cv.waitKey(30) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()