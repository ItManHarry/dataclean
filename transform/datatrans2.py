'''
1. dataframe调用apply方法来使用自定义函数进行数据处理
2. apply函数中axis 0表示行操作，1表示列操作
3. astype进行数据转换
4. map函数进行数据转换
'''
import pandas as pd
import os
os.chdir(r'D:\Development\Python\Dataclean\data')
df = pd.read_csv('sam_tianchi_mum_baby.csv', encoding='utf-8', dtype=str)
print(df.head(10))
print('-' * 80)
def gender(x):
    if x == '0':
        return 'F'
    elif x == '1':
        return 'M'
    else:
        return 'UnKnown'
# 使用自定义转换函数
df['gender_str'] = df['gender'].apply(gender)
print(df.head(10))
print(df[df['gender'] == '2'])
# 使用map函数
df['gender_str_2'] = df['gender'].map({'0': 'M', '1': 'F', '2': 'Unknown'})
print(df.head(10))
df['gender_str_3'] = df['gender'].map(gender)
print(df.head(10))
def encryt_id(id):
    return id.replace(id[1: 3], '**')
df['user_id'] = df['user_id'].apply(lambda id: id.replace(id[1: 3], '**'))
print(df.head(10))
a = '13780924007'
print(a.replace(a[3: 7], '****'))
# df['birthday'] = df['birthday'].apply(lambda d: d[0: 4])
# print(df.head(10))