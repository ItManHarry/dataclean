'''
数据整理
    定义：数据清洗过程中，将不用的数据整理在一起，方便后续的分析，这个过程也称之为数据合并：
    方法：
        1. 堆叠：横向堆叠 、 纵向堆叠
        2. 主键合并：类似SQL里的关联操作
    concat([df1, df2, df3, ...], axis=1/0, ignore_index=True)
    axis=1:横向拼接 axis=0:纵向拼接
    ignore_index:忽略各个指标索引
    merge(left=df1, right=df2, how='inner/outer', left_on=column_name, right_on=column_name)
    join='inner':交集 join='outer':并集
'''
import numpy as np
import pandas as pd
import xlrd2
import os
os.chdir(r'D:\Development\Python\Dataclean\data')
print(os.getcwd())
order1 = pd.read_excel('meal_order_detail.xlsx', sheet_name='meal_order_detail1')
order2 = pd.read_excel('meal_order_detail.xlsx', sheet_name='meal_order_detail2')
order3 = pd.read_excel('meal_order_detail.xlsx', sheet_name='meal_order_detail3')
print(order1.shape, order1.size)
print(order2.shape, order2.size)
print(order3.shape, order3.size)
# 纵向合并
order_all = pd.concat([order1, order2, order3], axis=0, ignore_index=True)
print(order_all.shape, order_all.size)
print(order_all)
# 循环读取Excel各个sheet
workbook = xlrd2.open_workbook('meal_order_detail.xlsx')
sheets = workbook.sheet_names()
print(sheets)
data = pd.DataFrame()
for sheet in sheets:
    sheet_data = pd.read_excel('meal_order_detail.xlsx', sheet_name=sheet)
    data = pd.concat([sheet_data, data], ignore_index=True)
print(data)
print('-' * 80)
# 横向合并
df1 = pd.read_csv('baby_trade_history.csv', dtype={'user_id': str})
print('Baby trade history data shape : ', df1.shape)
df2 = pd.read_csv('sam_tianchi_mum_baby.csv', dtype={'user_id': str})
print('Baby info data shape : ', df2.shape)
df_merge = pd.merge(left=df1, right=df2, how='inner', left_on='user_id', right_on='user_id')
print('Merge data shape : ', df_merge.shape)
print(df_merge.head(10))