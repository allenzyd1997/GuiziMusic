# -*- coding:utf-8 -*-  

import sys
import re
import csv
import pymysql
import pandas as pd

#连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='gz_musicdb', charset='utf8')
cursor=conn.cursor()

sqlr="select song_id from songinfo"
df=pd.read_sql(sql=sqlr,con=conn)
csvfile=open('precomment.csv','w',newline='',encoding='UTF-8')
csv_write = csv.writer(csvfile)

for items in df.values:
    csv_write.writerow([str(items[0])])
    print(items)