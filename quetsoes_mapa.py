
from sklearn.utils import shuffle
import pandas as pd
import scipy.stats as stats
import numpy as np
import matplotlib as plt

data = pd.read_parquet("new.parquet")

# ============= mapa ser mais defesa ou ataque (winrole) =============



collum = np.zeros(data["mapname"].unique().size)
attacker_win_per_map = pd.DataFrame(columns=["map", "percentage"])

for map in data["mapname"].unique():
    map_info = data.query("mapname == '" + (str)(map) + "'")["winrole"]
    values = np.zeros(1000)
    for i in range(1000):
        sample = shuffle(map_info)[:30]
        attacker_win = sample.value_counts()["Attacker"]
        values[i] = attacker_win / 30
        attacker_win_per_map.loc[len(attacker_win_per_map)] = [map, values[i]]
    
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

for map in attacker_win_per_map["map"].unique():
    attacker_win_per_map.query("map == '" + map + "'").hist(column="percentage", by="map", grid=False)
    
    
## Influencia do Mapa no lado vencedor


#  Idealmente, os atacantes deveriam vencer 50% das vezes. Mapas que não cumprem essa média significam que eles favorecem um lado acima do outro.

#  Para verificar os mapas que favorecem um lado, usamos o teste da permutação para verificar em média quantas vitórias os atacantes tiveram por mapa.

#  O intervalo de confiança calculado nos garante que se O valor de 50% estiver no IC, então o mapa é equilibrado (não favorece um lado).

#- Atacantes Favorecidos: COASTLINE, HOUSE, FAVELAS, CHALET
#- Equilibrados: CLUB_HOUSE, YACHT, BORDER, SKYSCRAPER, BARTLETT_U, KAFE_DOSTOYEVSKY
#- Defensores Favorecidos: PLANE, KANAL, HEREFORD_BASE, CONSULATE, OREGON, BANK, 
