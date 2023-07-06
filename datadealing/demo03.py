'''
异常值处理
1. 异常值指的是偏离正常范围的值，不是错误值
2. 异常值出现的频率较低，但又对实际项目分析造成偏差
3. 异常值一般用过箱线图法（分为差法）或在分布图（标准差法）来判断
4. 异常值往往采用盖帽法或者数据离散化
'''
import numpy as np
import pandas as pd
import os
os.chdir(r'D:\Development\Python\Dataclean\data')
df = pd.read_csv('MotorcycleData.csv', encoding='gbk', na_values='Na')
df['Price'] = df['Price'].apply(lambda e: float(str(e).replace('$', '').replace(',', '').strip()))
print(df['Price'].head(10))
# 分位差判断
p_avg = df['Price'].mean()
p_std = df['Price'].std()
print(any(df['Price'] > p_avg + 2 * p_std))
print(any(df['Price'] < p_avg - 2 * p_std))
print(df['Price'].describe())
# 分布图判断
Q1 = df['Price'].quantile(q=0.25)
Q3 = df['Price'].quantile(q=0.75)
IQR = Q3 - Q1
print(any(df['Price'] > Q3 + 1.5*IQR))
print(any(df['Price'] > Q1 - 1.5*IQR))