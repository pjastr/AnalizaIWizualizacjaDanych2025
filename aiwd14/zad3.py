import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

hr = pd.read_csv("hr13.csv", sep=";", decimal=",")
dosw = hr["Lata_doświadczenia_zawodowego"]
print(np.min(dosw))
print(np.max(dosw))
dosw_pop = dosw[dosw >0]
plt.hist(dosw_pop, bins=5, edgecolor="black")
plt.title("Lata doświadczenia zawodowego")
plt.savefig("zad3.pdf")
plt.show()