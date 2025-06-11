# B12 - zad3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

travel = pd.read_csv("travel12.csv", delimiter=";").T
travel2 = travel.iloc[1:,].copy()
travel2.columns = travel.iloc[0,:]
travel2["Włochy"] = travel2["Włochy"].astype(float)