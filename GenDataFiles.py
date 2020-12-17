import datetime
import calendar
import random
import numpy
import pandas as pd
import uuid

products = {
  'Euro1': [75.00, 2000],
  'Remont': [21.00, 200],
  'Hlam': [1.5, 100]
  }

columns = ['ID', 'Date', 'Product', 'Price', 'Distribution']

def generate_random_time(month):
  day = generate_random_day(month)
  if random.random() < 0.5:
    date = datetime.datetime(2020, month, day,12,00)
  else:
    date = datetime.datetime(2020, month, day,20,00)
  time_offset = numpy.random.normal(loc=0.0, scale=180)
  final_date = date + datetime.timedelta(minutes=time_offset)
  return final_date.strftime("%m/%d/%y %H:%M")

def generate_random_day(month):
  day_range = calendar.monthrange(2020,month)[1]
  return random.randint(1,day_range)

###Создать список контрагентов

def generate_random_agents():
  agent_names = ['Producer_', 'Retail_', 'L_opperator_', 'P_opperator_']
  levels = ['ID1<ID1', 'ID1<ID2', 'ID1<ID3', 'ID1<ID4',
            'ID1>ID1', 'ID1>ID2', 'ID1>ID3', 'ID1>ID4',
            'ID2<ID1', 'ID2<ID2', 'ID2<ID3', 'ID2<ID4',
            'ID2>ID1', 'ID2>ID2', 'ID2>ID3', 'ID2>ID4',
            'ID3<ID1', 'ID3<ID2', 'ID3<ID3', 'ID3<ID4',
            'ID3>ID1', 'ID3>ID2', 'ID3>ID3', 'ID3>ID4',
            'ID4<ID1', 'ID4<ID2', 'ID4<ID3', 'ID4<ID4',
            'ID4>ID1', 'ID4>ID2', 'ID4>ID3', 'ID4>ID4',]
  levels = pd.unique(levels)

  cities = ['Kyiv', 'Dnepr', 'Lviv']
  #weights = [7, 4, 4]
  weights = numpy.round((numpy.random.permutation(32)+32)/9).astype(int).tolist()
  zips = ['01000', '49000', '79000']
  state = ['Kyivska', 'Dnipropetrovska', 'Lvivska']

  agent = random.choice(agent_names)
  #quantity = numpy.random.geometric(p=1.0-(1.0/product_price), size=1)[0]
  quantity = numpy.random.randint(50, 300)
  index = random.choices(range(len(levels)), weights=weights)[0]

  #return f"{agent}{random.randint(1,100)},  {levels[index]}, {quantity}, {cities[index]}, {state[index]} {zips[index]}"
  return f"{agent}{random.randint(1,25)},  {levels[index]}, {quantity}"
  #return f"{levels[index]}, {quantity}"


###
def create_data_csv():
  pass

def write_row(order_number, order_date, product, generate_random_agents):
  order_date= generate_random_time(month)
  product_price = products[product][0]
  output = [order_number, order_date, product, product_price, generate_random_agents]
  return output


if __name__ == '__main__':
  order_number = 2020
  for month in range(1,13):
    if month <= 10:
      #orders_amount = int(numpy.random.normal(loc=1200, scale=400))
      orders_amount = int(numpy.random.normal(loc=2400, scale=400))
    elif month == 11:
      #orders_amount = int(numpy.random.normal(loc=2000, scale=300))
      orders_amount = int(numpy.random.normal(loc=4000, scale=300))
    else: # month == 12
      #orders_amount = int(numpy.random.normal(loc=2600, scale=300))
      orders_amount = int(numpy.random.normal(loc=5200, scale=300))

    product_list = [product for product in products]
    weights = [products[product][1] for product in products]

    df = pd.DataFrame(columns=columns)
    print(orders_amount)

    i = 0
    while orders_amount > 0:

      agents = generate_random_agents()
      order_date = generate_random_time(month)

      product_choice = random.choices(product_list, weights)[0]
      df.loc[i] = write_row(order_number, order_date, product_choice, agents)
      i += 1

      # Add some items to orders with random chance
      if product_choice == 'Euro1':
        if random.random() < 0.15:
          df.loc[i] = write_row(order_number, order_date, "Remont", agents)
          i += 1

      elif product_choice == "Remont" or product_choice == "Hlam":

        if random.random() < 0.07:
          df.loc[i] = write_row(order_number, order_date, "Hlam", agents)
          i += 1

      if random.random() <= 0.02:
        product_choice = random.choices(product_list, weights)[0]
        df.loc[i] = write_row(order_number, order_date, product_choice, agents)
        i += 1

      if random.random() <= 0.002:
        df.loc[i] = columns
        i += 1

      if random.random() <= 0.003:
        df.loc[i] = ["","","","",""]
        i += 1

      order_number += 1
      orders_amount -= 1

    month_name = calendar.month_name[month]
    df.to_csv(f"Sales_{month_name}_2020.csv", index=False)
    print(f"{month_name} Complete")