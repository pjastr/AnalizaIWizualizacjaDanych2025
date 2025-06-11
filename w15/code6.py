import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sqlite3 import connect
conn = connect('hotele32.db')
data = pd.read_sql("SELECT * FROM hotele32", con=conn)
