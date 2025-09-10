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

from typing import Optional, List


def load_parquet(path: str, use_cols: Optional[List[str]] = None) -> pd.DataFrame:
    """Charge un parquet avec colonnes optionnelles (sélection insensible à la casse).

    - Toujours lire tout le fichier (ne jamais passer columns=... à read_parquet)
    - Sélectionner les colonnes demandées après lecture, en ignorant la casse
    - Les colonnes absentes sont ignorées avec un avertissement
    """
    df = pd.read_parquet(path)
    if not use_cols:
        return df

    # Mapping insensible à la casse -> nom original
    lower_map = {c.lower(): c for c in df.columns}
    selected_real = []
    for col in use_cols:
        key = col.lower()
        if key in lower_map:
            selected_real.append(lower_map[key])
        else:
            print(f"[WARN] Colonne demandée absente (ignorée): {col}")
    if not selected_real:
        print("[WARN] Aucune des colonnes demandées trouvée, retour complet.")
        return df
    return df[selected_real]