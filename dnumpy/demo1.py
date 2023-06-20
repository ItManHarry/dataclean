import numpy as np
a1 = np.array([1, 2, 3, 4, 5])
print(type(a1))
print(a1)
print(a1.ndim)
print(a1[0])
# 指定数据类型
a2 = np.array([1, 2, 3], dtype=str)
print(type(a2))
print(a2)
# 二维数据
a3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a3)
# 使用arange创建
a4 = np.arange(1, 20)
print(a4)
# 等差数组 - endpoint=True表示包含终止值
a5 = np.linspace(1, 10, 20, endpoint=True)
print(a5)
# 生成n行m列数据，如果只有一个参照就产生一维数组
a6 = np.zeros([4, 5])
print(a6)
a7 = np.zeros(4)
print(a7)
a8 = np.ones([2, 6])
print(a8)
# 每个元素加一
a8 += 1.5
print(a8)
# 数据方法一：维数
print(a8.ndim)
# 数据方法二：数组行列数
print(a8.shape)
# 数据方法三：数据大小
print(a8.size)
# 数据方法四：数据类型
print(a8.dtype)
# 数据访问
data = ((8.5, 6, 4, 1.2, 0.7), (1.5, 3.5, 4, 7.3, 9), (3.2, 4.5, 6, 3, 9), (11.2, 13.4, 15.6, 17.8, 19.5))
arr = np.array(data)
print(arr)
print(arr[3])
print(arr[0][0])
print(arr[2, 2])
