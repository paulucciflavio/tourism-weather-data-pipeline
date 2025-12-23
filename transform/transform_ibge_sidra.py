import pandas as pd

# 1. Ler dado bruto
df = pd.read_csv("data/raw/ibge_sidra_raw.csv")

# 2. Selecionar apenas colunas necessárias
df = df[["codigo_ibge", "municipio", "populacao", "ano"]]

# 3. Padronizar nome do município
df["municipio"] = (
    df["municipio"]
    .str.upper()
    .str.strip()
)

# 4. Garantir tipos corretos
df["codigo_ibge"] = df["codigo_ibge"].astype(int)
df["populacao"] = df["populacao"].astype(int)
df["ano"] = df["ano"].astype(int)

# 5. Validações básicas
assert df["codigo_ibge"].isna().sum() == 0, "Código IBGE nulo"
assert df["municipio"].isna().sum() == 0, "Município nulo"
assert df["populacao"].min() > 0, "População inválida"

# 6. Salvar dimensão
df.to_csv(
    "data/processed/dim_municipio.csv",
    index=False
)

print("TRANSFORM CONCLUÍDO COM SUCESSO")
print(df.head())
print(f"Total de municípios: {len(df)}")
