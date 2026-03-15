from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("model.pkl")

# Define request schema


class OrderRequest(BaseModel):
    num_of_item: int
    gender: int
    order_hour: int
    order_dayofweek: int


@app.post("/predict")
def predict(data: OrderRequest):
    features = np.array([[
        data.num_of_item,
        data.gender,
        data.order_hour,
        data.order_dayofweek
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }
