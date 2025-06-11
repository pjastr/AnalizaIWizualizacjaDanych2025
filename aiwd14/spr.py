import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Tworzymy ramkę danych
dane = {
    'x': [5, 15, 20, 25, 30],
    'y': [88, 67, 57, 46, 20]
}

df = pd.DataFrame(dane)

# 2. Rysujemy histogram
plt.figure(figsize=(5, 2))
plt.hist(
    df['x'][kat] for kat in df['x'],
    #bins=5,  liczba słupków, brak obramowanie słupków
    alpha=0.7  # przezroczystość dla lepszej estetyki
)
# 3. Oznaczenia i estetyka
labels = ['A', 'B', 'C', 'D', 'E']
plt.title('Wykres Słupki')
plt.xticks(ticks=5,
           labels=labels,
           rotation=45,
           ha='right')

plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()
