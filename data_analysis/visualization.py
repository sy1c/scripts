import pandas as pd
import matplotlib.pyplot as plt

# import data
path = ".\\data"
df = pd.read_csv(path + "\\df.csv")

fig, axs = plt.subplots(2, 1)
axs[0].plot(df["TIME"], df["A"])
axs[1].plot(df["TIME"], df["B"])

plt.show()