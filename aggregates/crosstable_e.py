import numpy as np
import pandas as pd
import os
import random
os.chdir(r'D:\Development\Python\Dataclean\data')
# genders = ['男', '女']
# handedness = ['左', '右']
# data = [[random.choice(genders), random.choice(handedness)] for i in range(100)]
# print(data)
# df = pd.DataFrame(data, columns=['Gender', 'Handedness'])
# print(df)
# df.to_csv('human_handedness_data.csv', encoding='gbk', index=False)
data = pd.read_csv('human_handedness_data.csv', encoding='gbk')
print(data)
cross_table = pd.crosstab(index=data['Gender'], columns=data['Handedness'], margins=True, margins_name='Total')
print(cross_table)
cross_table.to_csv('human_handedness_cross_table.csv', encoding='gbk')
cross_table.to_excel('human_handedness_cross_table.xlsx', sheet_name='data')