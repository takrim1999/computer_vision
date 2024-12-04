from ultralytics import YOLO
import cv2

# Load the pre-trained YOLO model
model = YOLO('yolov8n.pt')  # Replace with 'yolov5s.pt' if using YOLOv5

image_path = "input_image.jpg"
image = cv2.imread(image_path)

# Detect objects
results = model.predict(image, conf=0.5)  # conf: Confidence threshold

# Loop through detections and filter for 'person' class
for result in results:
    for box, class_id, confidence in zip(result.boxes.xyxy, result.boxes.cls, result.boxes.conf):
        if class_id == 0:  # 'person' class in COCO dataset
            x1, y1, x2, y2 = map(int, box)  # Bounding box
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Draw bounding box
            cv2.putText(image, f"Person {confidence:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Save the image with detections
cv2.imwrite("output_image.jpg", image)
