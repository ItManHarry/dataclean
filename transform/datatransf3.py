'''
字符串格式数据处理
'''
import pandas as pd
import os
os.chdir(r'D:\Development\Python\Dataclean\data')
df = pd.read_csv('MotorcycleData.csv', encoding='gbk')
print(df.info())
print(df['Price'].str[1: 3])
# df['Price'].astype('')
df['Price'] = df['Price'].str.strip('$').str.replace(',', '')
# df['Price'] = df['Price'].str.replace(',', '')
print(df['Price'])
df['Price'] = df['Price'].astype(int)
print(df.info())
s = ' $125,2635'
ns = s.strip().strip('$')
print(s)
print(ns)