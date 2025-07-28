import pickle
import pandas as pd

# import the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

#In real case scenario, get from ML Flow
MODEL_VERSION = '0.0.1'

# Model Class probabilities
class_labels = model.classes_.tolist()

def response(user_input: dict):
    df = pd.DataFrame([user_input])
    
    predicted_class = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }