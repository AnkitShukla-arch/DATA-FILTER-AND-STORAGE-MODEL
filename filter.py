import os
import sys
import pandas as pd

# --------------------------------------
# FIX: Add project root to Python path
# --------------------------------------
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(my_utils.py)

# Import from utils.py (same directory)
from utils import safe_makedirs
# If you renamed utils.py → my_utils.py, use:
# from my_utils import safe_makedirs


def main():
    output_dir = "filtered_output"
    safe_makedirs(output_dir)

    input_file = "data.csv"
    output_file = os.path.join(output_dir, "filtered_data.csv")

    if not os.path.exists(input_file):
        print(f"⚠️ Input '{input_file}' not found.")
        return

    df = pd.read_csv(input_file)
    df = df.dropna(how="all")
    df.to_csv(output_file, index=False)

    print(f"✅ Filtered output saved to {output_file}")


if __name__ == "__main__":
    main()
