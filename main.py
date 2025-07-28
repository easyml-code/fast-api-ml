from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.prediction_response import PredictionResponse
from schema.user_response import UserInput
from model.model import response, MODEL_VERSION, model

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Insurance API Working Good"}

@app.get("/health")
def health():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(data: UserInput):
    user_input = {
        'bmi':data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    print('\n\n', 'user_input', user_input, '\n\n\n')
    try:
        prediction = response(user_input)
        return JSONResponse(status_code=200, content={'prediction':prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message", str(e)})