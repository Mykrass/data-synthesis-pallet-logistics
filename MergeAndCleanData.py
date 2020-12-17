import os
import pandas as pd
import numpy as np

#
path = "./SalesData"
files = [file for file in os.listdir(path) if not file.startswith('.')]  # Ignore hidden files

all_months_data = pd.DataFrame()

for file in files:
    current_data = pd.read_csv(path + "/" + file)
    all_months_data = pd.concat([all_months_data, current_data])

all_months_data.to_csv("all_data.csv", index=False)
pd.read_csv('all_data.csv')

data_raw = pd.read_csv("all_data.csv")

data=data_raw.dropna().copy()

df = data[data['Price']!='Price'].copy()
df