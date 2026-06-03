from ultralytics import YOLO
import cv2
import numpy as np
import matplotlib.pyplot as plt

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("dataset/CAM 1.mp4")

x_points = []
y_points = []

frame_number = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

    # Process every 20th frame
    if frame_number % 20 != 0:
        continue

    results = model(frame, verbose=False)

    for box in results[0].boxes:

        if int(box.cls[0]) == 0:

            x1, y1, x2, y2 = box.xyxy[0]

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            x_points.append(center_x)
            y_points.append(center_y)

cap.release()

plt.figure(figsize=(10, 6))

plt.hist2d(
    x_points,
    y_points,
    bins=50
)

plt.colorbar()

plt.title("Customer Heatmap")

plt.savefig("output/heatmap_cam1.png")

print("Heatmap Saved")