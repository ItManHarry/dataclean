'''
数据排序：sort / argsort
数据搜索
'''
import numpy as np
s = np.array([1, 2, 3, 6.5, 10.3, 3.4, 20.4, 12.4])
print(s)
s = np.sort(s)
print(s)
for i in s:
    print(i)
# 二维数据排序，参数axis为0时，是按照列排序，为1时是按照行排序,默认为1
s = np.array([[2, 1, 5], [100, 34.5, 8], [102, 4, 29.5]])
print(s)
s = np.sort(s)
print(s)
s = np.sort(s, axis=0)
print(s)
# 查找 where函数:第一个为条件表达式，第二个是满足条件的返回值，第三个是不满足条件的返回值
ss = np.where(s > 30, s, 0)
print(ss)
print('-'*80)
# 筛选 extract函数：第一个为条件，第二个为返回值：不满足条件的会舍弃
ss = np.extract(s > 30, s)
print(ss)
print(ss.ndim)
print(ss.shape)
print(ss.size)