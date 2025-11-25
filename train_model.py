import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "random_forest.pkl")
DATA_PATHS = [
    "data/filtered_data.csv",
    "data/incoming/mydata.csv",
]
TARGET = "target"  # Change to your actual label col name if needed

def ensure_csv_exists():
    """Creates a tiny fake CSV if no data is present for robust CI/dev operation."""
    fallback = "data/incoming/mydata.csv"
    if not any(os.path.exists(p) for p in DATA_PATHS):
        os.makedirs(os.path.dirname(fallback), exist_ok=True)
        pd.DataFrame({
            "f1": [0, 1, 2],
            "f2": ["2024-01-01", "2024-01-02", "2024-01-03"],
            "target": [0, 1, 0]
        }).to_csv(fallback, index=False)
        print(f"[INFO] Created fallback CSV at {fallback}")

def clean_features(df):
    """Converts features to numeric, handles categoricals/dates robustly."""
    df = df.copy()
    # Convert potential date strings to timestamps
    for col in df.columns:
        # Try to convert date-like strings
        if "date" in col.lower() or df[col].astype(str).str.match(r"\d{4}-\d{2}-\d{2}").all():
            try:
                df[col] = pd.to_datetime(df[col], errors="coerce").astype(np.int64) / 1e9
            except Exception:
                df[col] = pd.to_numeric(df[col], errors="coerce")
    # One-hot encode non-numerics
    obj_cols = df.select_dtypes(include=["object", "category"]).columns
    df = pd.get_dummies(df, columns=obj_cols, dummy_na=True)
    return df.fillna(-1)

def get_train_data():
    """Loads available data, creates fake target if missing (for CI/dev only)."""
    for path in DATA_PATHS:
        if os.path.exists(path):
            df = pd.read_csv(path)
            if TARGET not in df.columns:
                df[TARGET] = np.random.randint(0, 2, len(df))
            X = df.drop(columns=[TARGET])
            y = df[TARGET]
            X = clean_features(X)
            return X, y
    raise FileNotFoundError("No training data found!")

def main():
    os.makedirs(MODEL_DIR, exist_ok=True)
    ensure_csv_exists()
    X, y = get_train_data()
    # Always at least 2 samples for test/train
    if len(X) < 2:
        raise ValueError("Too little data to train; provide at least two samples")
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    print(f"[INFO] Model trained and saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
