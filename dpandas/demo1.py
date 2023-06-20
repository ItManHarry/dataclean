import pandas as pd
# Series(data, index, dtype, name)
# data可以为列表、array或者dict
# index表示索引必须与数据长度相等
s1 = pd.Series((1, 24.5, 12.4, 45.8, 11.9))
print(s1)
print(type(s1))
print(s1.index)
s2 = pd.Series((1, 24.5, 12.4, 45.8, 11.9), index=['a', 'b', 'c', 'd', 'e'], name='Series1')
print(s2)
s3 = pd.Series(dict(a=100, b=24.5, c=23.6, d=200))
print(s3)
# 访问
print(s3[0])
print(s3[1:3])
print(s3['a'])
print(s3['a': 'c'])
# values方法
values = s3.values
print(values)
index = s3.index
print(index)