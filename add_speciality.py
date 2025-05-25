import pandas as pd

# Carrega o DataFrame
df = pd.read_parquet("dataset.parquet")  # ou o nome do seu arquivo atualizado

# Dicionário de especialidades (baseado no documento fornecido)
specialty_map = {
    "ASH": "breach", "THERMITE": "breach", "CASTLE": "anti-entry", "PULSE": "intel",
    "IQ": "intel", "BLITZ": "front line", "JAGER": "anti-gadget", "BANDIT": "anti-entry",
    "TWITCH": "anti-gadget", "MONTAGNE": "intel", "ROOK": "support", "DOC": "support",
    "FUZE": "anti-gadget", "GLAZ": "intel", "TACHANKA": "anti-entry", "KAPKAN": "anti-entry",
    "SLEDGE": "breach", "THATCHER": "anti-gadget", "SMOKE": "anti-entry", "MUTE": "anti-gadget",
    "BLACKBEARD": "breach", "VALKYRIE": "intel", "BUCK": "breach", "FROST": "anti-entry",
    "CAPITAO": "front line", "CAVEIRA": "intel", "HIBANA": "breach", "ECHO": "intel",
    "JACKAL": "intel", "MIRA": "intel"
}

# Extrai o nome do operador (removendo o prefixo antes do "-")
df["OPERATOR_NAME"] = df["operator"].str.split("-").str[-1]

# Mapeia a especialidade
df["SPECIALTY"] = df["OPERATOR_NAME"].map(specialty_map)

# Remove a coluna auxiliar
df.drop(columns=["OPERATOR_NAME"], inplace=True)

# Salva com a nova coluna
df.to_parquet("datadump_s5_specialty.parquet", index=False)
