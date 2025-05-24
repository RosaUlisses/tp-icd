import pandas as pd

parquet_file = "datadump_s5.parquet"
new = "new.parquet"

colunas_remover = [
    'primaryweapon', 'primaryweapontype', 'primarysight', 'primarygrip',
    'primaryunderbarrel', 'primarybarrel', 'secondaryweapon',
    'secondaryweapontype', 'secondarysight', 'secondarygrip',
    'secondaryunderbarrel', 'secondarybarrel', 'secondarygadget'
]

df = pd.read_parquet(parquet_file)

df.drop(columns=colunas_remover, inplace=True, errors='ignore')

df.to_parquet(new)