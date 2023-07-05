'''
聚合函数
'''
import numpy as np
import pandas as pd
import os
os.chdir(r'D:\Development\Python\Dataclean\data')
data = pd.read_csv('online_order.csv', encoding='gbk', dtype={'customer': str, 'order': str})
# print(data)
data_groupby = data.groupby('weekday')
# print(data_groupby)
data_agg = data_groupby.agg([np.max, np.mean, np.min])
print(type(data_agg))
data_agg.to_csv('online_order_agg_1.csv', encoding='utf-8')
data_agg = data_groupby[['total_items', 'discount%', 'hour', 'Fresh%', 'Drinks%']].agg([np.min, np.mean, np.max])
data_agg.to_csv('online_order_agg_2.csv', encoding='utf-8')
data_agg = data_groupby.agg({'total_items': np.sum, 'Food%': [np.mean, np.max, np.min]})
data_agg.to_csv('online_order_agg_3.csv', encoding='utf-8')
# 直接统计
data_agg = data[['total_items', 'Food%', 'Drinks%']].agg([np.max, np.mean, np.min, np.sum])
data_agg.to_csv('online_order_agg_4.csv', encoding='utf-8')
