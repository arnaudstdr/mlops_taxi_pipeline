mlops-taxi-pipeline/
│── data/
│   ├── raw/                 # Données brutes téléchargées
│   ├── processed/           # Données après preprocessing
│
│── notebooks/
│   ├── 01_eda_preprocessing.ipynb   # Notre premier notebook
│
│── src/
│   ├── __init__.py
│   ├── data_loader.py       # Téléchargement & préparation des données
│   ├── preprocessing.py     # Nettoyage, feature engineering
│   ├── utils.py             # Fonctions utilitaires
│
│── models/
│   ├── trained_models/      # Modèles sauvegardés
│
│── requirements.txt
│── README.md
│── .gitignore

