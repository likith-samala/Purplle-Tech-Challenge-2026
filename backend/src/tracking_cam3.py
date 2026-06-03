from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.track(
    source="dataset/CAM 3.mp4",
    tracker="bytetrack.yaml",
    save=True,
    conf=0.4,
    imgsz=320,
    vid_stride=5,
    project="output",
    name="tracking_cam3"
)

print("Tracking Completed")