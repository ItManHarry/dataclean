'''
read_csv()读取文件
to_csv()快速保存为csv文件
'''
import numpy as np
import pandas as pd
import os
print(os.getcwd())
os.chdir(r'D:\\Development\\Python\\Dataclean\\data')
print(os.getcwd())
data = pd.read_csv('sam_tianchi_mum_baby.csv', encoding='utf-8')
print(data)
print(data.head(10))
order_data = pd.read_csv('meal_order_info.csv', encoding='gbk', dtype=object)
print(order_data)
print('-' * 80)
print(order_data.info)
order_data.to_csv('new_data.csv', encoding='gbk', index=False)
print('Data saved to csv file successfully!')