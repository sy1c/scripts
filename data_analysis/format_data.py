import glob
import pandas as pd

# load data
path = ".\\data"
files = glob.glob(path + "\\*.csv")

dfs = []

for file in files:
    data = pd.read_csv(file)
    dfs.append(data)

# merge data frames
df = pd.concat(dfs, ignore_index=True)

# delete data from data frame
df = df.drop(df.iloc[:, 0:2], axis='columns')

# rename headers
df = df.rename(
    columns={
        "C": "A",
        "D": "B"})

print(df)