import pandas as pd

df_raw = pd.read_excel(
    "data/raw/ibge.xls",
    header=None
)

print(df_raw.head(15))

