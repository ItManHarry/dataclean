import numpy as np
a1 = np.array([1, 2, 3, 4, 5])
print(type(a1))
print(a1)
print(a1.ndim)
print(a1[0])
# 指定数据类型
print('-'*80)
a2 = np.array([1, 2, 3], dtype=str)
print(type(a2))
print(a2)
print('-'*80)
# 二维数据
a3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a3)
print('-'*80)
# 使用arange创建
a4 = np.arange(1, 20)
print(a4)
print('-'*80)
# 等差数组 - endpoint=True表示包含终止值
a5 = np.linspace(1, 10, 20, endpoint=True)
print(a5)
print('-'*80)
# 生成n行m列数据，如果只有一个参数就产生一维数组
a6 = np.zeros([4, 5])
print(a6)
a7 = np.zeros(4)
print(a7)
a8 = np.ones([2, 6])
print(a8)
# 每个元素加1.5
a8 += 1.5
print(a8)
# 数组属性1：维数
print(a8.ndim)
# 数组属性2：数组行列数
print(a8.shape)
# 数组属性3：数据大小(行数 * 列数)
print(a8.size)
# 数组属性：数据类型
print(a8.dtype)
print('-'*80)
# 数据访问
data = ((8.5, 6, 4, 1.2, 0.7), (1.5, 3.5, 4, 7.3, 9), (3.2, 4.5, 6, 3, 9), (11.2, 13.4, 15.6, 17.8, 19.5))
arr = np.array(data)
print(arr)
print(arr[3])
print(arr[0][0])
print(arr[2, 2])
print('-'*80)
for d in data:
    print(d)
    print('Data 0 is : ', d[0], d[1])