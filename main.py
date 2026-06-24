import os
import pandas as pd

def run_on_demand_prediction():
    input_path = "batch_prediction_dataset/on_demand_dataset.csv"
    print("====== Starting On-Demand Batch Prediction ======")
    
    if not os.path.exists(input_path):
        print(f"Error: Missing file {input_path}")
        return

    # 1. Read the CSV file
    
    df = pd.read_csv(input_path)
    
    # 2. Simple Rule-Based Classifier

    predictions = []
    for text in df['segments']:
        text_lower = str(text).lower()
        if "children" in text_lower or "primary" in text_lower or "alphabet" in text_lower:
            predictions.append("Key Stage 1-2")
        elif "secondary" in text_lower or "poem" in text_lower:
            predictions.append("Key Stage 3")
        elif "shakespeare" in text_lower or "analysis" in text_lower:
            predictions.append("Key Stage 4")
        else:
            predictions.append("Key Stage 5")
            
    # 3. Save the results

    df['predicted_stage'] = predictions
    df.to_csv(input_path, index=False)
    print(f"Success! Results saved perfectly to {input_path}")

if __name__ == "__main__":
    run_on_demand_prediction()