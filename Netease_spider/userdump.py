import pymysql
import pandas as pd
import time

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='gz_musicdb', charset='utf8')
cursor=conn.cursor()

sqlr="select user_id from userinfo"
df=pd.read_sql(sql=sqlr,con=conn)
count=0
for items in df.values:
    userid=items[0]
    password="$2a$10$Xtc6ECrZZQzC0e38l3btHuR8GI1LHCluF02v0OuGcKdcrPVbf57nq"
    sqlw='insert into user(id,username,password) values(%s,%s,%s);'
    try:
        cursor.execute(sqlw,[str(userid),str(userid),str(password)])
        #time.sleep(0.05)
        conn.commit()
    except Exception as e:
        print("增加用户失败",e)
    else:
        count+=1
        print("增加用户成功",count)
print("成功增加 ",count," 个用户，上传结束")
