import pandas as pd
from sqlite3 import connect
import matplotlib.pyplot as plt

conn = connect('parki13.db')
data = pd.read_sql("SELECT * FROM DANE", con=conn)
rok16 = data[data["Rok"]== 2016]
wojew = rok16.loc[37:]

cmap = plt.colormaps['Set3']
kolory = [cmap(i) for i in range(5)]

plt.pie(wojew["Wartosc"], labels=wojew["Nazwa"], colors=kolory, autopct="%1.1f%%")
plt.title("Dane o parkach w 2016")
plt.savefig("zad2.svg")
plt.show()