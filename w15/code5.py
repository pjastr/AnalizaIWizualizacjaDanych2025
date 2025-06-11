import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rod = pd.read_excel("rod15.xlsx", header=None).T
rod2 = rod.iloc[1:,].copy()
rod2.columns = rod.iloc[0,:]
rod2["Rok"] = rod2["Rok"].astype(int)
rod2["Wartosc"] = rod2["Wartosc"].astype(float)