import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

wyksz = pd.read_csv("wyksz62.csv")
wiek1 = wyksz[wyksz["Wiek"]=="13-19"]
wiek2 = wyksz[wyksz["Wiek"]=="20-24"]
wiek3 = wyksz[wyksz["Wiek"]=="25-29"]
x= wiek1["Wykształcenie"]
y1 = wiek1["Liczebność"]
y2 = wiek2["Liczebność"]
y3 = wiek3["Liczebność"]
plt.bar(x, y1)
plt.bar(x, y2, bottom = y1)
plt.bar(x, y3, bottom = y1.to_numpy()+y2.to_numpy())
plt.show()