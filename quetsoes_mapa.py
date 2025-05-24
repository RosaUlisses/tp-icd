# 'mapname', 'objectivelocation', 'winrole', 'endroundreason', 'roundduration', 'operator'
# operadores mais usados por mapa

import pandas as pd

data = pd.read_parquet("new.parquet")


# ============= objetivos mais jogados por mapa =============

objective_per_map = data[["mapname", "objectivelocation", "endroundreason"]]
objective_per_map = objective_per_map.groupby(["mapname", "objectivelocation"]).count()
print(objective_per_map)


# ============= mapa ser mais defesa ou ataque (winrole) =============

winrole_per_map = data[["mapname", "winrole"]]
total_count = winrole_per_map.groupby("mapname").count()
defender_wins = (
    winrole_per_map.query("winrole == 'Defender'").groupby("mapname").count()
)
attacker_wins = (
    winrole_per_map.query("winrole == 'Attacker'").groupby("mapname").count()
)
print(defender_wins.head())
print(attacker_wins.head())


# ============= motivos por vitoria no mapa (duracao do round) =============

reason_victory = data[["mapname", "endroundreason", "roundduration"]]
reason_victory = reason_victory.groupby(["mapname", "endroundreason"]).mean()
print(reason_victory)
