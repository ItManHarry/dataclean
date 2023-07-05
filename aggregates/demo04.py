'''
透视表：根据行列对数据进行各个维度的汇总
    pivot_table(data, index, columns, values, aggfunc, fill_value, margins, margins_name)
    index:行分组键
    columns: 列分组键
    values: 分组的字段，只能为数值型数据
    aggfunc:聚合函数
    margins：是否需要总计
交叉表：用于频数的分析
    crosstab(index, columns, normalize)
    inde:行索引
    columns：列索引
    normalize：是否进行标准化处理 ： index：行占比 columns:列占比
'''
import numpy as np
import pandas as pd
import os
os.chdir(r'D:\Development\Python\Dataclean\data')
print(os.getcwd())
df = pd.read_csv('online_order.csv', encoding='gbk', dtype={'customer': str, 'order': str})
print(df.columns)
# p_t = pd.pivot_table(df, index='weekday', columns='customer', values=['total_items', 'hour'], aggfunc=[np.mean, np.sum], margins=True, margins_name='Sum', fill_value=0)
p_t = pd.pivot_table(df, index='weekday', values=['total_items', 'hour'], aggfunc=[np.mean, np.sum], margins=True, margins_name='Sum', fill_value=0)
# print(p_t)
p_t.to_csv('online_order_pivot_table.csv', encoding='utf-8')
# 交叉表
c_t0 = pd.crosstab(index=df['weekday'], columns=df['discount%'], margins=True, margins_name='合计')
c_t1 = pd.crosstab(index=df['weekday'], columns=df['discount%'], margins=True, margins_name='合计', normalize='index')
c_t2 = pd.crosstab(index=df['weekday'], columns=df['discount%'], margins=True, margins_name='合计', normalize='columns')
print(c_t0)
print(c_t1)
print(c_t2)
