'''
缺失值处理
1. 缺失值首先需要根据实际情况定义
2. 可以采取直接删除法
3. 有时候需要使用替换法或者插值法
4. 常用的替换法有均值替换、前项、后项和常量替换
pd.dropna()
pd.fillna()
'''
import numpy as np
import pandas as pd
import os
os.chdir(r'D:\Development\Python\Dataclean\data')
print(os.getcwd())
df = pd.read_csv('MotorcycleData.csv', encoding='gbk')
print(df)
null_percent = df.apply(lambda x: sum(x.isnull())/len(x), axis=0)
# print(type(null_percent))
# print('Shape is : ', null_percent.shape)
# for n in null_percent:
#     print('Null percent is : ', n)
# n_a_values = [[n] for n in null_percent]
# n_a_columns = [column for column in df.columns]
# print(n_a_values)
# print(n_a_columns)
# data = dict(zip(n_a_columns, n_a_values))
# print(data)
# df_null = pd.DataFrame(data=data)
# print(df_null.shape)
# df_null.to_csv('MotorcycleData_Null.csv', encoding='utf-8', index=False)
# df = pd.concat([df, df_null], ignore_index=True)
# # df.insert(loc=1, value=null_percent, column=df.columns)
# print(df)
# df.to_csv('MotorcycleData_Null_Append.csv', encoding='utf-8', index=False)
print('Before delete na data : ', df.shape[0])
df.dropna(how='any', subset=['Condition', 'Price', 'Mileage'], inplace=True)
print('After delete na data : ', df.shape[0])
df.to_csv('MotorcycleData_Dropped_NA.csv', encoding='gbk', index=False)
# 填充默认值
df = pd.read_csv('MotorcycleData.csv', encoding='gbk', na_values='Na')
df['Mileage'] = df['Mileage'].apply(lambda e: float(str(e).replace(',', '').strip()))
df.fillna(value={'Exterior_Color': df['Exterior_Color'].mode(), 'Mileage': df['Mileage'].median()}, inplace=True)
df.to_csv('MotorcycleData_Fill_NA1.csv', encoding='gbk', index=False)
# 前项填充
df = pd.read_csv('MotorcycleData.csv', encoding='gbk', na_values='Na')
df['Exterior_Color'].fillna(method='ffill', inplace=True)
df.to_csv('MotorcycleData_Fill_NA_F.csv', encoding='gbk', index=False)
# 后项填充
df = pd.read_csv('MotorcycleData.csv', encoding='gbk', na_values='Na')
df['Exterior_Color'].fillna(method='bfill', inplace=True)
df.to_csv('MotorcycleData_Fill_NA_B.csv', encoding='gbk', index=False)