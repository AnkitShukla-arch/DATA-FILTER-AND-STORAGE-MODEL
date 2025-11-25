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
TARGET = "target"  # Change this to your actual target column if needed

def clean_features(df, drop_cols=None):
    """Converts every column except TARGET to numeric (including datetimes)."""
    df = df.copy()
    # 1. If any drop columns are specified (e.g. IDs), drop
    if drop_cols:
        df = df.drop(columns=[c for c in drop_cols if c in df.columns])
    # 2. Convert date/datetime columns to timestamp float
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]) or df[col].astype(str).str.match(r"^\d{4}-\d{2}-\d{2}").all():
            try:
                df[col] = pd.to_datetime(df[col], errors="coerce").astype(np.int64) / 1e9
            except Exception:
                df[col] = pd.to_numeric(df[col], errors="coerce")
    # 3. One-hot encode all remaining non-numeric columns
    non_numeric = df.select_dtypes(include=["object", "category"]).columns.tolist()
    if non_numeric:
        df = pd.get_dummies(df, columns=non_numeric, dummy_na=True)
    # 4. Fill any remaining NaN with -1
    df = df.fillna(-1)
    return df

def get_train_data():
    """Find a CSV, split features/target, auto-synth target if missing."""
    for path in DATA_PATHS:
        if os.path.exists(path):
            df = pd.read_csv(path)
            if TARGET not in df.columns:
                # Auto-add fake label for demonstration/testing
                df[TARGET] = np.random.randint(0, 2, len(df))
            drop = [col for col in ["id", "ID", "index"] if col in df.columns]
            X = df.drop(columns=[TARGET] + drop)
            y = df[TARGET]
            X = clean_features(X, drop_cols=drop)
            return X, y
    raise FileNotFoundError(f"No data found in {DATA_PATHS}")

def main():
    os.makedirs(MODEL_DIR, exist_ok=True)
    X, y = get_train_data()
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    print(f"[INFO] Trained model saved to {MODEL_PATH} (Features: {X.shape[1]})")

if __name__ == "__main__":
    main()
