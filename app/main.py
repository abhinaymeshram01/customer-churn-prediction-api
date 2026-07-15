from fastapi import FastAPI
import joblib
import pandas as pd
from app.schema import CustomerData
from app.utils import create_feature

app = FastAPI(
    title='Customer Churn Predication API',
    version='1.0'
)

pipeline = joblib.load('model/churn_pipeline.pkl')

@app.get('/')
def hi():
    return {"message": "Customer Churn Prediction API is Running"}

@app.post('/predict')
def predict(data: CustomerData):

    df = pd.DataFrame([data.model_dump()])
    df = create_feature(df)

    prediction = pipeline.predict(df)[0]

    probability = pipeline.predict_proba(df)[0][1]

    threshold = 0.45

    result = 'Yes' if prediction >= threshold else 'No'

    return {
        'prediction': result,
        'Churn Probability': round(float(probability)),
        'Threshold': threshold
    }