'''
创建数据库连接
conn = create_engine('mysql_pymysql://user:password@ip:3306/test01')
df.to_sql(name, con=conn, if_exists='replace/append/fail', index=False)
name:表名
conn: 数据库连接
if_exists: 表如果存在的处理方式，append：数据追加；replace:删除源表，重建，fail:不做操作
'''
import pandas as pd
from sqlalchemy import create_engine
conn = create_engine('mysql+pymysql://itam:Itam2022@10.41.128.217:3306/itam')
sql = 'select * from biz_asset_master'
data_master = pd.read_sql(sql, con=conn)
print(data_master)
data_master.to_sql('biz_asset_master_bak', con=conn, index=False, if_exists='replace')
print('Data save to mysql successfully!!!')