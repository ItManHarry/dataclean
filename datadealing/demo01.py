'''
重复值处理
1. 数据清洗一般从重复值和缺失值开始处理
2. 重复值一般采用删除法进行处理
3. 有的重复值是不能删除的，比如订单明细等
df[df.duplicated()]
np.sum(df.duplicated())
df.drop_duplicates()
df.drop_duplicates(subset=[...], inplace=True)
'''
import numpy as np
import pandas as pd
import os
os.chdir(r'D:\Development\Python\Dataclean\data')
df = pd.read_csv('MotorcycleData.csv', encoding='gbk', dtype={'Price': str, 'Mileage': str}, na_values='Na')
print(df.head(10))
print(df.columns)
print(df.info())
def to_float(s):
    if not isinstance(s, str):
        s = str(s)
    s = s.replace('$', '').replace(',', '')
    return float(s.strip())
df['Price'] = df['Price'].apply(to_float)
df['Mileage'] = df['Mileage'].apply(to_float)
print(df[['Price', 'Mileage']].head(10))
print(df.info())
# 判断是否有重复数据
print(any(df.duplicated()))
# 查看重复数据
print(df[df.duplicated()])
duplicated_data = df[df.duplicated()]
duplicated_data.to_csv('MotorcycleData_Duplicated.csv', encoding='gbk', index=False)
print(np.sum(df.duplicated()))
# 去除重复值
df.drop_duplicates(inplace=True)
df.to_csv('MotorcycleData_Clean1.csv', encoding='gbk', index=False)
# 根据某几列判断重复值并剔除
print(np.sum(df.duplicated(subset=['Condition', 'Condition_Desc', 'Price', 'Location'])))
df.drop_duplicates(subset=['Condition', 'Condition_Desc', 'Price', 'Location'], inplace=True)
df.to_csv('MotorcycleData_Clean2.csv', encoding='gbk', index=False)