from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("dataset/CAM 3.mp4")

max_people = 0
frame_number = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

    # Process every 10th frame
    if frame_number % 10 != 0:
        continue

    results = model(frame, verbose=False)

    current_people = 0

    for box in results[0].boxes:
        cls = int(box.cls[0])

        if cls == 0:  # person
            current_people += 1

    max_people = max(max_people, current_people)

    print(f"Frame {frame_number}: {current_people} people")

cap.release()

print("\n========== ANALYTICS ==========")
print("Maximum People Visible:", max_people)
print("Analysis Completed")