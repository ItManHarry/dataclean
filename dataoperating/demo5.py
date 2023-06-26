'''
层次索引-多索引
在一个轴上拥有两个或两个以上的索引
- 使用loc函数进行访问
- loc函数接受元组参数，如：loc[(a, b, ...), : ]
'''
import os
import pandas as pd
os.chdir(r'D:\Development\Python\Dataclean\data')
print(os.getcwd())
# index_col设置索引列
df = pd.read_csv('baby_trade_history.csv', dtype={'user_id': str}, index_col=[3, 0])
print(df.head(10))
print('-' * 80)
print(df.loc[28])
print('-' * 80)
print(df.loc[([28, 38])])
print('-' * 80)
print(df.loc[([28, 38], ['532110457', '377550424', '321032222', '21224132']), ['auction_id', 'cat_id', 'day']])