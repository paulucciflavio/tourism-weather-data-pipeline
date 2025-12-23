import pandas as pd
from sqlalchemy import create_engine

# conexão com o banco
engine = create_engine(
    "postgresql://postgres:123456@localhost:5432/weather_db"
)

# lendo o CSV transformado
df = pd.read_csv("data/processed/dim_municipio.csv")

# carregando no banco
df.to_sql(
    "dim_municipio",
    engine,
    if_exists="append",  # NÃO replace agora
    index=False
)

print("LOAD concluído com sucesso!")
