from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.predict(
    source="dataset/CAM 3.mp4",
    save=True,
    project="output",
    name="cam3_detection",
    conf=0.4,
    imgsz=320,
    vid_stride=5
)

print("Detection Completed")