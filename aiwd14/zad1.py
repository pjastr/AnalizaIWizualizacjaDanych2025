import matplotlib.pyplot as plt
import numpy as np

y = np.arange(4)
x1 = [20,41, 18, 42]
x2 = [10,22,41,24]
x3 = [63,70,60,57]
plt.barh(y-0.25, x1, height = 0.25, color = "gray", label="A")
plt.barh(y, x2, height = 0.25, color = "orange", label="B")
plt.barh(y+0.25, x3, height = 0.25, color = "olive", label="C")
plt.title("Wykres")
plt.legend()
plt.yticks(y,["PL","DE","FR","SK"])
plt.grid(True)
plt.ylabel("Podpis osi 1", color="red")
plt.xlabel("Podpis osi 2", color="green")
plt.savefig("zad1.tiff")
plt.show()