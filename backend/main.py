from fastapi import FastAPI
import json
from backend.logic import unlocked_layers
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "questions.json")) as f:
    questions = json.load(f)

@app.post("/questions")
def get_questions(answers:dict):
    layers = unlocked_layers(answers)

    result = []
    for layer in layers:
        result.extend(questions[layer])

    return result