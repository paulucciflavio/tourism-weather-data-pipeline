import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 1. Lê o arquivo bruto de população
population_raw = pd.read_csv(
os.path.join(base_dir, "data", "raw", "population_raw.csv")
)

# 2. Padroniza o nome do código do município
population_raw = population_raw.rename(columns={
    "codigo_municipio": "codigo_ibge"
})

# 3. Cria o identificador único do município
population_raw["city_id"] = population_raw["codigo_ibge"].astype(str)

# 4. Seleciona apenas as colunas necessárias
population_clean = population_raw[
    ["city_id", "municipio", "populacao"]
]

# 5. Renomeia colunas para padrão final
population_clean = population_clean.rename(columns={
    "municipio": "city_name",
    "populacao": "population"
})

# 6. Salva o arquivo padronizado
population_clean.to_parquet(
    "staging/population_clean.parquet",
    index=False
)
