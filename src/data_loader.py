import os
import urllib.request
import pandas as pd

RAW_DIR = os.path.join(os.path.dirname(__file__), "../data/raw")
os.makedirs(RAW_DIR, exist_ok=True)

def download_month(month: str, year: str = "2023") -> str:
    """Télécharge un fichier Parquet du dataset Taxi NYC pour un mois donnée."""
    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month}.parquet"
    local_path = os.path.join(RAW_DIR, f"yellow_tripdata_{year}-{month}.parquet")
    if not os.path.exists(local_path):
        print(f"🔄 Téléchargement {year}-{month}...")
        urllib.request.urlretrieve(url, local_path)
    else:
        print(f"✅ Déjà téléchargé : {local_path}")
    return local_path

def load_parquet(path: str, use_cols: list[str] = None) -> pd.DataFrame:
    """Charge un parquet avec colonnes optionnelles."""
    return pd.read_parquet(path, columns=use_cols)