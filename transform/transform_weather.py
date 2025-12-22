import json
from pathlib import Path
from datetime import datetime
import pandas as pd

# ==============================
# CAMINHOS
# ==============================

RAW_DATA_PATH = Path("data/raw")
PROCESSED_DATA_PATH = Path("data/processed")

PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

# ==============================
# FUNÇÃO DE TRANSFORMAÇÃO
# ==============================

def transform_weather_data():
    records = []

    for file in RAW_DATA_PATH.glob("weather_*.json"):
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        record = {
            "city": data.get("name"),
            "datetime": datetime.fromtimestamp(data.get("dt")),
            "temperature_c": data.get("main", {}).get("temp"),
            "humidity": data.get("main", {}).get("humidity"),
            "weather_description": data.get("weather", [{}])[0].get("description"),
            "wind_speed": data.get("wind", {}).get("speed")
        }

        records.append(record)

    df = pd.DataFrame(records)

    output_file = PROCESSED_DATA_PATH / "weather_processed.csv"
    df.to_csv(output_file, index=False)

    print(f"Dados transformados salvos em: {output_file}")

# ==============================
# EXECUÇÃO
# ==============================

if __name__ == "__main__":
    transform_weather_data()
