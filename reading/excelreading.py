import numpy as np
import pandas as pd
import os
os.chdir(r'D:\\Development\\Python\\Dataclean\\data')
data1 = pd.read_excel('meal_order_detail.xlsx', sheet_name=0)
# pd.set_option('column', 10)
print(data1)
data1.to_excel('new_meal_order_detail.xlsx', index=False, sheet_name='one')
print('Save excel file successfully!!!')