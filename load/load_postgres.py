import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# ==============================
# CONFIGURAÇÕES DO BANCO
# ==============================

DB_USER = "postgres"
DB_PASSWORD = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "weather_db"

# ==============================
# CAMINHO DO CSV
# ==============================

PROCESSED_DATA_PATH = Path("data/processed/weather_processed.csv")

# ==============================
# FUNÇÃO DE LOAD
# ==============================

def load_to_postgres():
    df = pd.read_csv(PROCESSED_DATA_PATH)

    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    df.to_sql(
        name="weather_data",
        con=engine,
        if_exists="append",
        index=False
    )

    print("Dados carregados com sucesso no PostgreSQL")

# ==============================
# EXECUÇÃO
# ==============================

if __name__ == "__main__":
    load_to_postgres()
