import numpy as np
x = np.arange(15, dtype=np.int64).reshape(3, 5)
print(x)
print(x.max(axis=1))
print(x.max(axis=0))
print('-' * 80)
x = np.array([[1, 2, 5, 8], [10, 3, 40, 30], [20, 10, 5, 7], [23, 43, 4, 40]])
print(x)
print(x.max(axis=0))
print(x.max(axis=1))