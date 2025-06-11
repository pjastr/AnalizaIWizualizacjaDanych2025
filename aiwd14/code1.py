import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("kawa.csv", parse_dates=["Data"], dayfirst=False)

x = df["Data"]
y = df["Liczba sprzedanych kaw"]

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', linewidth=2)

plt.title("Liczba sprzedanych kaw w dniach 1–7 czerwca 2025", fontsize=14)
plt.xlabel("Data", fontsize=12)
plt.ylabel("Liczba sprzedanych kaw", fontsize=12)

plt.grid(True, linestyle='--', alpha=0.7)

# zapisanie daty na podziałce X w fromacie dd.mm.yyyy
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gcf().autofmt_xdate()

plt.tight_layout()
plt.show()