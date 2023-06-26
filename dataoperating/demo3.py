'''
数据修改和查找
1. rename修改列名或行索引
2. loc方法修改数据
3. loc方法查找数据
4. '&' 与 ; '|' 或
5. between和isin选择满足添加的行
'''
import os
import numpy as np
import pandas as pd
os.chdir(r'D:\\Development\\Python\\Dataclean\\data')
df = pd.read_csv('sam_tianchi_mum_baby.csv', encoding='utf-8', dtype=str)
print(df.head(10))
print(df.info())
df.loc[df['gender'] == '0', 'gender '] = '女'
df.loc[df['gender'] == '1', 'gender '] = '男'
df.loc[df['gender'] == '2', 'gender '] = '未知'
print(df.head(10))
df.rename(columns={'user_id': '用户ID', 'birthday': '生日', 'gender': '性别'}, inplace=True)
print(df.head(10))
df.rename(index={3: 12333, 4: 12344}, inplace=True)
print(df.head(10))
print(df.iloc[:5])
df.reset_index(drop=True, inplace=True)
print(df.head(10))
# 查询
df = pd.read_csv('baby_trade_history.csv')
print(df.head(10))
df1 = df[df['buy_mount'] > 10]
print(df1.head(10))
df2 = df[~(df['buy_mount'] > 10)]
print(df2.head(10))
df3 = df[(df['buy_mount'] > 10) & (df['day'] > 20140101)]
print(df3.head(10))
df4 = df[df['buy_mount'].between(4, 10, inclusive='both')]
print(df4.head(10))
df5 = df[df['cat1'].isin([28, 38])]
print(df5.head(10)['cat1'])