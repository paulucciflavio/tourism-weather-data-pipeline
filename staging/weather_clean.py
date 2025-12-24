import json
import pandas as pd
import os

# Descobre a pasta raiz do projeto
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho do arquivo bruto
input_path = os.path.join(base_dir, "data", "raw", "weather_raw.json")

# Caminho do arquivo de saída
output_path = os.path.join(base_dir, "staging", "weather_clean.parquet")

# Lê o JSON bruto (uma cidade)
with open(input_path, "r", encoding="utf-8") as f:
    item = json.load(f)

# Cria um único registro
record = {
    "city_id": item["id"],
    "temperature": item["main"]["temp"],
    "humidity": item["main"]["humidity"],
    "weather_main": item["weather"][0]["main"],
    "timestamp": item["dt"]
}

# Converte para DataFrame
weather_clean = pd.DataFrame([record])

# Salva em parquet
weather_clean.to_parquet(output_path, index=False)

print("Arquivo weather_clean.parquet criado com sucesso.")

