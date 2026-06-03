from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Purplle Store Intelligence System"
    }

@app.get("/report")
def get_report():

    with open("output/report.json", "r") as file:
        data = json.load(file)

    return data

@app.get("/footfall")
def footfall():

    return {
        "totalPersonDetections": 436,
        "averagePeopleVisible": 0.98,
        "maxPeopleVisible": 5
    }

@app.get("/health")
def health():

    return {
        "status": "running"
    }