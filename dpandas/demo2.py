import pandas as pd
from pandas import DataFrame
import numpy as np
# pandas.DataFrame(data, index, dtype, columns)
# data可以为列表、array或者dict
# index表示索引必须与数据长度相等, columns表示列标签
df1 = DataFrame([['Jack', 23, 'M'], ['Tom', 25, 'M'], ['Jane', 30, 'F'], ['Bill', 25, 'M']], columns=['姓名', '年龄', '性别'])
print(df1)
df2 = DataFrame({'Name': ['Harry', 'Jane', 'Tom'], 'Age': [25, 35, 24], 'Gender': ['M', 'F', 'M']})
print(df2)
data = np.array([['Jack', 23, 'M'], ['Tom', 25, 'M'], ['Jane', 30, 'F'], ['Bill', 25, 'M']])
df3 = DataFrame(data, columns=['Name', 'Age', 'Gender'], index=['a', 'b', 'c', 'd'])
print(df3)
print('-'*80)
# values
values = df3.values
print(values)
index = df3.index
print(index)
print(df3.shape)
print(df3.ndim)
print(df3.size)
print(df3.dtypes)