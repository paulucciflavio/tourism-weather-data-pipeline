import requests
import json
from datetime import datetime
from pathlib import Path

# ==============================
# CONFIGURAÇÕES
# ==============================

API_KEY = "5a228665697d1e1f853bc9ea6dd6f743"
CITY = "Rio de Janeiro"
COUNTRY_CODE = "BR"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# ==============================
# CAMINHO PARA SALVAR OS DADOS
# ==============================

RAW_DATA_PATH = Path("data/raw")
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

# ==============================
# FUNÇÃO DE EXTRAÇÃO
# ==============================

def extract_weather_data():
    params = {
        "q": f"{CITY},{COUNTRY_CODE}",
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Erro na API: {response.status_code}")

    data = response.json()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"weather_{CITY.replace(' ', '_').lower()}_{timestamp}.json"
    file_path = RAW_DATA_PATH / file_name

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    print(f"Dados salvos com sucesso em: {file_path}")

# ==============================
# EXECUÇÃO
# ==============================

if __name__ == "__main__":
    extract_weather_data()
