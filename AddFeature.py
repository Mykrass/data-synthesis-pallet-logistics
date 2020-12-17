# ADD CITY COLUMN
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


#df['Levels'] = df['Distribution'].apply(lambda x: f"{get_city(x)} {get_state(x)}")
df['Quantity'] = df['Distribution'].apply(lambda x: f"{get_quantity(x)}")
#df['City'] = df['Distribution'].apply(lambda x: f"{get_city(x)}")
#df['State'] = df['Distribution'].apply(lambda x: f"{get_state(x)}")
df['Partner'] = df['Distribution'].apply(lambda x: f"{get_partner(x)}")
df['Way'] = df['Distribution'].apply(lambda x: f"{get_way(x)}")
df