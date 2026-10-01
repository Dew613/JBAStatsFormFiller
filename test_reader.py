import os
import pandas as pd
import yaml

# Load file name from yaml
if os.path.exists("config.yaml"):
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
        excel_file = config.get("excel_filename")
else:
    print("Error: config.yaml not found.")
    excel_file = None

# Check if file exists
if excel_file and os.path.exists(excel_file):
    print(f"Found '{excel_file}' from config.yaml")
    print("Reading data ... \n")

    # Load file and preview data
    df = pd.read_excel(excel_file)

    print("====== Column Headers ======")
    print(df.columns.tolist())
    print("====== First 3 rows ======")
    print(df.head(3))  
else:
    print(f"Could not find the file '{excel_file}' specified in config.yaml.")
