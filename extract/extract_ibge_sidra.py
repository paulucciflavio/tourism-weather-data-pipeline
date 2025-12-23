import requests
import pandas as pd

URL = "https://apisidra.ibge.gov.br/values/t/6579/n6/all/v/9324/p/last?formato=json"

response = requests.get(URL)
data = response.json()

# Converter JSON em DataFrame
df = pd.DataFrame(data)

# Remover a linha de metadata
df = df.iloc[1:].reset_index(drop=True)

# Renomear colunas corretas
df = df.rename(columns={
    "D1C": "codigo_ibge",
    "D1N": "municipio",
    "V": "populacao",
    "D3N": "ano"
})

# Selecionar colunas finais
df = df[["codigo_ibge", "municipio", "populacao", "ano"]]

# Converter tipos
df["codigo_ibge"] = df["codigo_ibge"].astype(int)
df["populacao"] = df["populacao"].astype(int)
df["ano"] = df["ano"].astype(int)

print(df.head())
print(f"Total de municípios: {len(df)}")
# Salvar dados brutos extraídos
df.to_csv(
    "data/raw/ibge_sidra_raw.csv",
    index=False
)
