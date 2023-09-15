import os
import pandas as pd
os.chdir(r'C:\Users\20112004\Desktop\tmp')
print(os.getcwd())
data = pd.read_csv(r'斗山名称修改.csv', encoding='gbk', dtype=object)
print(data)
procedures = []
for item in data.values:
    if item[0] not in procedures:
        procedures.append(item[0])
print(procedures)
data = pd.DataFrame(procedures)
print(data)
data.to_csv(r'斗山名称修改_去重.csv', encoding='gbk')