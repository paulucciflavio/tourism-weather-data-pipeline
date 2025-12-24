import pandas as pd
import os

# Descobre a pasta raiz do projeto
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho do arquivo de entrada (staging)
input_path = os.path.join(base_dir, "staging", "population_clean.parquet")

# Caminho do arquivo de saída (gold)
output_path = os.path.join(base_dir, "gold", "dim_city.parquet")

# Lê os dados limpos de população
population = pd.read_parquet(input_path)

# Cria a dimensão de cidades (apenas o que existe)
dim_city = (
    population[["city_id", "city_name"]]
    .drop_duplicates()
    .rename(columns={
        "codigo_ibge": "city_id",
        "municipio": "city_name"
    })
    .sort_values("city_id")
    .reset_index(drop=True)
)

# Salva a dimensão
dim_city.to_parquet(output_path, index=False)

print("Arquivo dim_city.parquet criado com sucesso.")
