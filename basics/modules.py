import random, datetime, os, json, math, pandas as pd
from math import sqrt, pi


intgr = random.randint(1, 10)
sel_fruit = random.choice(['banana', 'apple', 'orange'])

curr_datetime = datetime.date.today()

curr_dir = os.getcwd()

data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_data = json.dumps(data)

root_res = sqrt(16)
radius = 5
circle_area = pi * radius ** 2

df = pd.DataFrame(data)
print(intgr)
print(sel_fruit)  
print(curr_datetime)
print(curr_dir)
print(json_data)
print(root_res)
print(circle_area)
print(df)