import pandas as pd

FEATS_KEEP = [
    "trip_duration_minutes",
    "trip_distance", "passenger_count",
    "PULocationID", "DOLocationID",
    "pickup_hour", "pickup_dow", "is_weekend",
    "RatecodeID", "payment_type",
    "fare_amount", "tip_amount", "tolls_amount", "total_amount"
]

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoyage + feature engineering."""

    # Converion datetime
    df["pickup_dt"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["dropoff_dt"] = pd.to_datetime(df["tpep_dropoff_datetime"])

    # Cible : durée de trajet
    df["trip_duration_minutes"] = (df["dropoff_dt"] - df["pickup_dt"]).dt.total_seconds() / 60

    # Features temporelles
    df["pickup_hour"] = df["pickup_dt"].dt.hour
    df["pickup_dow"] = df["pickup_dt"].dt.dayofweek
    df["is_weekend"] = df["pickup_dow"].isin([5, 6]).astype(int)

    # Filtrage outliers
    mask = (
        (df["trip_duration_minutes"].between(1, 180, inclusive="both")) &
        (df["trip_distance"].between(0.1, 100, inclusive="both")) &
        (df["fare_amount"].between(0.1, 300, inclusive="both")) &
        (df["passenger_count"].fillna(1).between(1, 6, inclusive="both"))
    )

    df = df[mask].copy()

    return df[FEATS_KEEP]