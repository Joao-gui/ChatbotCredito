# FastAPI - https://fastapi.tiangolo.com/

import joblib
import pandas as pd
from fastapi import FastAPI

# Inicializar a API
app = FastAPI(title="API de crédito", version="1.0")

# Carregar modelo
model = joblib.load("models/modelo_credito.pkl")

# Rota inicial
@app.get("/")
def home():
    return {"Message": "API de Crédito rodando."}

# Rota de previsão
@app.post("/predict")
def predict(data: dict):
    try:
        df = pd.DataFrame([data])

        prediction = model.predict(df)[0]
        probability0 = model.predict_proba(df)[0][0]
        probability1 = model.predict_proba(df)[0][1]

        return {
            "predicao": int(prediction),
            "probabilidade_0": float(probability0),
            "probabilidade_1": float(probability1)
        }

    except Exception as e:
        return {"error": str(e)}