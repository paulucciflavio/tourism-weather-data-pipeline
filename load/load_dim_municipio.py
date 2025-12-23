import pandas as pd
from sqlalchemy import create_engine

# 1. Configurações do banco (AJUSTE SE NECESSÁRIO)
USER = "postgres"
PASSWORD = "123456"
HOST = "localhost"
PORT = "5432"
DB = "weather_db"

engine = create_engine(
    f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
)

# 2. Ler CSV processado
df = pd.read_csv("data/processed/dim_municipio.csv")

# 3. Carregar no PostgreSQL
df.to_sql(
    "dim_municipio",
    engine,
    if_exists="replace",   # recria a tabela
    index=False
)

print("LOAD CONCLUÍDO COM SUCESSO")
print(f"Registros inseridos: {len(df)}")
