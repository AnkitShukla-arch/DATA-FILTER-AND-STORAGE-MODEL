import os
import pandas as pd
# Change this line based on your final filename choice 👇
from utils import safe_makedirs  
# If the name conflict persists, rename file to my_utils.py and change this to:
# from my_utils import safe_makedirs

def main():
    # Example of where filtered data will be stored
    output_dir = "filtered_output"
    
    # Ensure output directory exists
    safe_makedirs(output_dir)
    
    # Example filter logic
    input_file = "data.csv"
    output_file = os.path.join(output_dir, "filtered_data.csv")

    if not os.path.exists(input_file):
        print(f"⚠️ Input file '{input_file}' not found. Skipping filter step.")
        return

    # Load data
    df = pd.read_csv(input_file)

    # Example cleaning logic
    df = df.dropna(how="all")  # remove empty rows

    # Save output
    df.to_csv(output_file, index=False)
    print(f"✅ Filtered data saved to {output_file}")

if __name__ == "__main__":
    main()
