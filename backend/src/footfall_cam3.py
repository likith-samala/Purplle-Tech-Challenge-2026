from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("dataset/CAM 3.mp4")

total_frames = 0
total_people_detections = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    total_frames += 1

    if total_frames % 10 != 0:
        continue

    results = model(frame, verbose=False)

    current_people = 0

    for box in results[0].boxes:

        if int(box.cls[0]) == 0:
            current_people += 1

    total_people_detections += current_people

cap.release()

avg_people = round(total_people_detections / (total_frames // 10), 2)

print("\n========== FOOTFALL REPORT ==========")
print("Frames Processed:", total_frames)
print("Total Person Detections:", total_people_detections)
print("Average People Visible:", avg_people)
print("====================================")