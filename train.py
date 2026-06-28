import json
import os



def train_and_store():
    print("====== Executing CD Training Pipeline ======")
    
    # Simple simulated model metrics structure
    
    model_metadata = {
        "model_type": "DistilBERT-UK-Stage-Classifier",
        "status": "Trained",
        "epochs": 2,
        "accuracy": 0.824
    }
    
    # Make sure the 'models' directory exists

    os.makedirs("models", exist_ok=True)
    
    # Store the model artifact metadata inside the models folder

    with open("models/model_artifacts.json", "w") as f:
        json.dump(model_metadata, f, indent=4)
        
    print("CD Pipeline success! Model weights simulated and stored in models/ folder.")

if __name__ == "__main__":
    train_and_store()
