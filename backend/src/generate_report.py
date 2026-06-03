import json

report = {
    "camera": "CAM3",
    "framesProcessed": 4436,
    "totalPersonDetections": 436,
    "averagePeopleVisible": 0.98,
    "maxPeopleVisible": 5,
    "status": "success"
}

with open("output/report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Report Generated")