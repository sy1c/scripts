import glob
import pandas as pd

path = ".\\data"
files = glob.glob(path + "\\*.csv")

dfs = []

for file in files:
    data = pd.read_csv(file)
    dfs.append(data)

df = pd.concat(dfs, ignore_index=True)

print(df)