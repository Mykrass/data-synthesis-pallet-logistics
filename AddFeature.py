# ADD COLUMN
import os
import pandas as pd
import numpy as np
#
def get_partner(distribution):
  return distribution.split(",")[0].strip(" ")

def get_way(distribution):
  return distribution.split(",")[1].split(" ")[2]

def get_quantity(distribution):
  return distribution.split(",")[2].strip(" ")

def get_city(distribution):
  return distribution.split(",")[3].strip(" ")

def get_state(distribution):
  return distribution.split(",")[4].strip(" ").split(" ")[0]

#
df = pd.read_csv('df.csv')
#df['Levels'] = df['Distribution'].apply(lambda x: f"{get_city(x)} {get_state(x)}")
df['Quantity'] = df['Distribution'].apply(lambda x: f"{get_quantity(x)}")
#df['City'] = df['Distribution'].apply(lambda x: f"{get_city(x)}")
#df['State'] = df['Distribution'].apply(lambda x: f"{get_state(x)}")
df['Partner'] = df['Distribution'].apply(lambda x: f"{get_partner(x)}")

df['Way'] = df['Distribution'].apply(lambda x: f"{get_way(x)}")

df['Key'] = df['Way'].str[-4:-3]
dictionary = {'<':-1, '>':1}
df['Key'].map(dictionary)

df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.date
df['Day_of_year'] = df['Date'].dt.dayofyear
df['Month'] = df['Date'].dt.month_name()
df['Week_of_year'] = df['Date'].dt.isocalendar().week
df['Weekday'] = df['Date'].dt.day_name()
df= df[df['Weekday']!='Saturday']
df= df[df['Weekday']!='Sunday']
df['Hour'] = pd.to_datetime(df['Date']).dt.hour
df['Minute'] = pd.to_datetime(df['Date']).dt.minute
df['Quantity'] = pd.to_numeric(df['Quantity']) * df['Key'].map(dictionary)
df['Price'] = pd.to_numeric(df['Price'])
df['Sales'] = df['Quantity'] * df['Price']
df= df[df['Hour']>7]
df= df[df['Hour']<19]
df.to_csv('Sinthetic_Data.csv', index=False)