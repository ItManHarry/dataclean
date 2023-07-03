'''
1. to_datetime()方法将文本格式转换为日期格式
2. 数据类型为datetime64的，使用dt方法获取对应的年月日
3. 对于时间差数据，使用timedelta函数将其转换为指定时间单位的数值
'''
import pandas as pd
import numpy as np
import os
from datetime import datetime
os.chdir(r'D:\Development\Python\Dataclean\data')
print(os.getcwd())
df = pd.read_csv('baby_trade_history.csv', encoding='utf-8', dtype={'user_id': str})
print(df.info())
# to_datetime()
df['buy_day'] = pd.to_datetime(df['day'], format='%Y%m%d', errors='coerce')
print(df.info())
# 年月份分别提取
print(df['buy_day'].dt.year)
print(df['buy_day'].dt.month)
print(df['buy_day'].dt.day)
# 时间差
df['diff_day'] = datetime.now() - df['buy_day']
print(df.head(10))
print(df['diff_day'].dt.days)
print(df['diff_day'].dt.seconds)
print(df['diff_day'].dt.microseconds)
df['diff_days'] = df['diff_day']/pd.Timedelta('1 D')
df['diff_minutes'] = df['diff_day']/pd.Timedelta('1 S')
print(df.head(10))
df['diff_day'].astype('timedelta64[s]')
print(df.head(10))