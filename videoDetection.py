# Open video capture
from ultralytics import YOLO
import cv2

def resizeFrame(frame,scale=0.5):
    newDimension =  (int(frame.shape[1]*scale),int(frame.shape[0]*scale))
    resizedFrame = cv2.resize(frame,newDimension,interpolation=cv2.INTER_AREA)
    return resizedFrame


# Load the pre-trained YOLO model
model = YOLO('yolov8n.pt')  # Replace with 'yolov5s.pt' if using YOLOv5


cap = cv2.VideoCapture("Resources/Videos/HumanWalking.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect objects
    results = model.predict(frame, conf=0.3)

    # Loop through detections and filter for 'person' class
    for result in results:
        for box, class_id, confidence in zip(result.boxes.xyxy, result.boxes.cls, result.boxes.conf):
            if class_id == 0:  # 'person' class in COCO dataset
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(frame, f"Person {confidence:.2f}", (x1, y1 - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the frame
    cv2.imshow("Human Detection", resizeFrame(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
