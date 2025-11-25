import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "random_forest.pkl")
DATA_PATHS = [
    "data/filtered_data.csv",            # output from your filter or pipeline
    "data/incoming/mydata.csv",          # fallback
]
TARGET = "target"  # adjust if your label column is named differently

def get_train_data():
    """Looks for a valid input CSV and returns (X, y) for modeling."""
    for path in DATA_PATHS:
        if os.path.exists(path):
            df = pd.read_csv(path)
            if TARGET not in df.columns:
                # Fallback: add synthetic target for demonstration
                df[TARGET] = np.random.randint(0, 2, len(df))
            X = df.drop(columns=[TARGET])
            y = df[TARGET]
            return X, y
    raise FileNotFoundError(f"No source CSV found in {DATA_PATHS}")

def main():
    os.makedirs(MODEL_DIR, exist_ok=True)
    X, y = get_train_data()
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    print(f"[INFO] Model trained and saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
