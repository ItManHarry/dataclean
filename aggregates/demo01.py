'''
分组函数groupby:
df.groupby(by=)
统计方法：count/mean/median/max/min等
'''
import pandas as pd
import os
os.chdir(r'D:\Development\Python\Dataclean\data')
print(os.getcwd())
df = pd.read_csv('online_order.csv', encoding='gbk', dtype={'customer': str, 'order': str})
print(df.head(5))
# 按照weekday分组
grouped = df.groupby('weekday')
print(type(grouped))
# 平均值
print(type(grouped['total_items'].mean()))
# 多列分组
grouped = df.groupby(by=['customer', 'weekday'])
print(grouped.sum()['total_items'])
print(grouped['total_items'].sum())
totals = grouped.sum()['total_items']
print(type(totals))
new_df = pd.DataFrame(totals)
print(new_df)
new_df.to_csv('online_sum_data.csv')
grouped = grouped[['total_items', 'hour']].sum()
print(type(grouped))
grouped.to_csv('online_total_data.csv')