import pandas as pd
import os
os.chdir(r'D:\Development\Python\Dataclean\data')
print(os.getcwd())
data = pd.read_csv('baby_trade_history.csv', encoding='gbk', dtype={'user_id': str})
print(data)
print('-' * 80)
print(data.info())
print(data.columns)
# 读取列
print(data[['user_id', 'cat_id', 'property']])
print('-' * 80)
print('First column data : ', data.loc[0])
print('-' * 80)
print(data.loc[3: 4])
print('-' * 80)
print(data.loc[:, ['user_id', 'cat_id']])
print('-' * 80)
print(data.loc[1: 3, ['user_id', 'cat_id']])
print('-' * 80)
print(data.loc[(data.user_id == '532110457') | (data.buy_mount > 100), ['user_id', 'cat_id', 'buy_mount']])
print('-' * 80)
print(data.iloc[1:3])
print('-' * 80)
print(data.iloc[:, 1: 4])
print('-' * 80)
print(data.iloc[1: 10, [0, 3]])
'''
iloc&loc的区别
loc[2: 7]:标签过滤，包含2和7
iloc[2: 7]:范围过滤，包含2不包含7
'''
print('-' * 80)
print(data.loc[2: 7])
print('-' * 80)
print(data.iloc[2: 7])