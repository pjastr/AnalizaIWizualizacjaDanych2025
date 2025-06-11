import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.DataFrame({
'Sklep': ['Sklep A'] * 5 + ['Sklep B'] * 5 + ['Sklep C'] * 5,
'Cena (zł/kg)': [3.5, 3.6, 3.7, 3.4, 3.8,
3.9, 4.0, 3.8, 4.1, 3.7,
4.2, 4.1, 4.3, 4.0, 4.2]
})

groups = df1["Sklep"].unique()
shops = [df1[df1['Sklep'] == shop]['Cena (zł/kg)'] for shop in groups]
plt.boxplot(shops)
plt.show()