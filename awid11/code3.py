import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Wczytanie danych
df = pd.read_csv('dataset/wiek.csv')

# Przygotowanie wartości
male = -df['Mężczyźni']
female = df['Kobiety']
age_groups = df['Grupa wiekowa']
plt.figure(figsize=(8, 6))
plt.barh(age_groups, male, label='Mężczyźni')
plt.barh(age_groups, female, label='Kobiety')

# Definicja ticków co 2000, od -8000 do +8000, i wyświetlenie ich jako wartości bezwzględnych
ticks = np.arange(-8000, 8001, 2000)
labels = np.abs(ticks)
plt.xticks(ticks, labels)

plt.xlabel('Liczba osób')
plt.ylabel('Grupa wiekowa')
plt.title('Piramida wieku populacji')

plt.legend()
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()