import cv2
import numpy
from ultralytics import YOLO
 
model = YOLO('yolo11n.pt')

def resizeFrame(frame,scale=0.5):
    newDimension =  (int(frame.shape[1]*scale),int(frame.shape[0]*scale))
    resizedFrame = cv2.resize(frame,newDimension,interpolation=cv2.INTER_AREA)
    return resizedFrame



myImage = cv2.imread('Resources/Photos/personAndDog.jpg')
results = model.predict(myImage,conf=0.3)
new_image = numpy.zeros(myImage.shape)





for result in results:
    for box,class_id,confidence in zip(result.boxes.xyxy,result.boxes.cls,result.boxes.conf):
        # print()
        x1,y1,x2,y2 = map(int,box)
        myImage = cv2.rectangle(myImage,(x1,y1),(x2,y2),(0,255,0),2)
        myImage = cv2.circle(myImage,(int((x1+x2)/2),int((y1+y2)/2)),2,(0,0,255))
        myImage = cv2.putText(myImage,f"{result.names[int(class_id)]} {confidence:0.2f}",(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2) 
cv2.imshow('Person Box Image',resizeFrame(myImage))
cv2.waitKey(0)