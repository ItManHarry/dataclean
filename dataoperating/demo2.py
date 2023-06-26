'''
数据新增和删除
'''
import pandas as pd
import numpy as np
import os
os.chdir(r'D:\\Development\\Python\\Dataclean\\data')
# 插入列 dataframe.insert
df = pd.read_csv('baby_trade_history.csv')
print(df.head(10))
df['购买量'] = np.where(df['buy_mount'] > 3, '高', '低')
print(df.head(30))
auction_column = df['auction_id']
print(auction_column)
del df['auction_id']
df.insert(0, 'auction_id', auction_column)
print(df.head(10))
# 删除数据 drop(labels, axis, inplace=True) / del
# 删除列 axis=1
df2 = df.drop(labels=['auction_id', '购买量'], axis=1)
df.drop(labels=['auction_id', '购买量'], axis=1, inplace=True)
print(df.head(10))
print(df2.head(10))
# 删除行 axis=0 labels=行级索引
df.drop(labels=[3, 4], axis=0, inplace=True)
print(df.head(10))
df.drop(labels=range(6, 11), axis=0, inplace=True)
print(df.head(10))