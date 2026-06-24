# Project Report: MLOps Final Assignment

## Objective

Classify literary text segments into the "UK Key Stage" (the corresponding
stage of the UK school system), using a fine-tuned DistilBERT model trained on
a balanced dataset.

## Repository structure

- `model/model.ipynb`: training notebook. Loads `database/model1/TRAIN_balanced.csv`
  and `TEST_balanced.csv`, encodes the labels, tokenizes with `DistilBertTokenizer`,
  and trains a `DistilBertForSequenceClassification` for 2 epochs, logging the
  experiment with MLflow (`UK_Key_Stage_Classification`).
- `database/model1/`: training and test datasets (class-balanced).
- `train.py`: continuous delivery (CD) pipeline script. Simulates training and
  stores the model metadata in `models/model_artifacts.json`.
- `main.py`: on-demand batch prediction script. Uses a simple rule-based
  classifier (keyword matching) over `batch_prediction_dataset/on_demand_dataset.csv`
  to assign a stage to each segment.
- `.github/workflows/cd_pipeline.yml`: CI/CD pipeline that runs on every push
  to `main`, installs dependencies, and runs `train.py`.

## CI/CD pipeline

The `Model Training CD Pipeline` workflow runs on `ubuntu-latest`, sets up
Python 3.10, and executes `train.py`. The latest run (commit `d473d7c`)
completed successfully.

## Results

The notebook trains with a high batch size and only 2 epochs, so modest
results are expected (see the metrics reported by `trainer.evaluate()` inside
the notebook). The CD pipeline's `train.py` uses simulated metrics
(`accuracy: 0.824`) as a placeholder for the real training run.

## Notes and pending items

- The trained model is not currently saved as an artifact (the
  `model.save_pretrained` / `tokenizer.save_pretrained` lines are commented out
  in the notebook).
- `train.py` simulates the training step; it does not run the notebook or
  produce a real model inside the CI pipeline.
