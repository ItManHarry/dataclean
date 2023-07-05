'''
分组对象与apply函数
注意：axis参数的意义 0：表示沿着行求值 1：表示沿着列求值
'''
import pandas as pd
import numpy as np
import os
os.chdir(r'D:\Development\Python\Dataclean\data')
df = pd.read_csv('online_order.csv', encoding='gbk', dtype={'customer': str, 'order': str})
print(df.columns)
group_data = df.groupby('weekday')
print(group_data['hour'].sum())
apply_data = group_data['hour'].apply(np.mean)
print(apply_data)
vars = ['Food%', 'Fresh%', 'Drinks%', 'Home%', 'Beauty%', 'Health%', 'Baby%', 'Pets%']
print(df[vars].apply(np.sum, axis=0))   # 行求和，即每一列求和，最后结果是行数等于列数
print(df[vars].apply(np.sum, axis=1))   # 列求和，即每一行求和，最后结果是行数不变
print(df[vars].apply(lambda x: x[0]-x[1], axis=1))