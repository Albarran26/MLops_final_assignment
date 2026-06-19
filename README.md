# MLops_final_assignment

Este repositorio ya no depende de Kaggle para cargar el dataset del notebook.

## Estructura

- `model/model.ipynb`: notebook de entrenamiento con DistilBERT
- `database/model1/TRAIN_balanced.csv`: dataset de entrenamiento
- `database/model1/TEST_balanced.csv`: dataset de evaluacion

## Como usarlo

1. Crea y activa un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Abre el notebook:

```bash
jupyter notebook model/model.ipynb
```

## Notas

- El notebook busca los CSV en `database/model1` de forma local.
- Si quieres mover el dataset a otra carpeta, define la variable de entorno `UK_KEY_STAGE_DATA_DIR`.
- La primera vez que ejecutes el notebook, `transformers` descargara `distilbert-base-uncased` desde Hugging Face si no esta ya cacheado.
