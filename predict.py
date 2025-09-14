import joblib
import numpy as np
import argparse
import json
from sklearn.datasets import load_iris

def load_model(path="iris_rf_model.pkl"):
    return joblib.load(path)

def predict(model, sample):
    sample = np.array(sample).reshape(1, -1)
    pred = model.predict(sample)
    probs = model.predict_proba(sample) if hasattr(model, "predict_proba") else None
    return int(pred[0]), (probs[0].tolist() if probs is not None else None)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="iris_rf_model.pkl")
    parser.add_argument("--sample", type=str,
                        help='JSON list of 4 features, e.g. "[5.1,3.5,1.4,0.2]"')
    args = parser.parse_args()

    model = load_model(args.model)
    sample = json.loads(args.sample)
    pred, probs = predict(model, sample)
    iris = load_iris()
    print({"predicted_class_index": pred,
           "predicted_class_name": iris.target_names[pred].tolist(),
           "probabilities": probs})
