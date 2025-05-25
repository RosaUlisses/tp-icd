import pandas as pd
import scipy.stats as stats
import numpy as np

data = pd.read_parquet("new.parquet")


# ============= objetivos mais jogados por mapa =============
#
# objective_per_map = data[["mapname", "objectivelocation", "endroundreason"]]
# objective_per_map = objective_per_map.groupby(["mapname", "objectivelocation"]).count()
# print(objective_per_map)
#

# ============= mapa ser mais defesa ou ataque (winrole) =============


collum = np.zeros(data["mapname"].unique().size)
attacker_win_per_map = pd.DataFrame(
    {"percentage": collum}, index=data["mapname"].unique()
)
for map in attacker_win_per_map.index:
    map_info = data.query("mapname == '" + (str)(map) + "'")
    values = np.zeros(1000)
    for i in range(1000):
        map_info = map_info.sample(frac=1)
        sample = map_info[:100]
        sample = sample.query("winrole == 'Attacker'")["winrole"]
        values[i] = sample.size / 100

    print("Map: " + map)
    print(
        "CI: "
        + (str)(
            stats.t.interval(
                0.95,
                df=len(values) - 1,
                loc=np.mean(values),
                scale=np.std(values, ddof=1) / np.sqrt(len(values)),
            )
        )
    )
    print("")


#
# winrole_per_map = data[["mapname", "winrole"]]
# total_count = winrole_per_map.groupby("mapname").count()
# defender_wins = (
#     winrole_per_map.query("winrole == 'Defender'").groupby("mapname").count()
# )
# attacker_wins = (
#     winrole_per_map.query("winrole == 'Attacker'").groupby("mapname").count()
# )
# print(defender_wins.head())
# print(attacker_wins.head())
#
#
# # ============= motivos por vitoria no mapa (duracao do round) =============
#
#
# reason_victory = data[["mapname", "endroundreason", "roundduration"]]
# reason_victory = reason_victory.groupby(["mapname", "endroundreason"]).mean()
#
# print(reason_victory)
