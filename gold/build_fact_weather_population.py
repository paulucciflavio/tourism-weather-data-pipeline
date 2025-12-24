import pandas as pd
import os

# Descobre a pasta raiz do projeto
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminhos de entrada
population_path = os.path.join(base_dir, "staging", "population_clean.parquet")
weather_path = os.path.join(base_dir, "staging", "weather_clean.parquet")

# Caminho de saída
output_path = os.path.join(base_dir, "gold", "fact_weather_population.parquet")

# Lê os dados
population = pd.read_parquet(population_path)
weather = pd.read_parquet(weather_path)

# Padroniza o tipo do city_id
population["city_id"] = population["city_id"].astype(int)
weather["city_id"] = weather["city_id"].astype(int)

# Join entre população e clima
fact = population.merge(
    weather,
    on="city_id",
    how="inner"
)

# Seleciona apenas colunas que EXISTEM
fact = fact[
    [
        "city_id",
        "city_name",
        "population",
        "temperature",
        "humidity",
        "weather_main",
        "timestamp"
    ]
]

# Salva a tabela fato
fact.to_parquet(output_path, index=False)

print("Arquivo fact_weather_population.parquet criado com sucesso.")


