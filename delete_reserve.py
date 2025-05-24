import pandas as pd

# Carrega o DataFrame (supondo que você já tenha ele em parquet ou CSV)
df = pd.read_parquet("dataset.parquet")  # ou pd.read_csv("seuarquivo.csv")

# Remove as linhas onde a coluna 'operator' termina com 'RESERVE'
df_filtrado = df[~df["operator"].str.endswith("RESERVE")]

# (Opcional) Salva o DataFrame filtrado novamente
df_filtrado.to_parquet("datadump.parquet", index=False)