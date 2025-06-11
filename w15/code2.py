# B12 - zad3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

travel = pd.read_csv("travel12.csv", delimiter=";", index_col=0).T