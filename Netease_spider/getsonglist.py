#-*-coding:utf-8-*- 
import requests
import csv
import pandas as pd
import json
import time
import types
import pymysql
import codecs

#连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='gz_musicdb', charset='utf8')
cursor=conn.cursor()
#存数据到数据库


# 获取歌手id和歌手姓名
def read_csv():

    with open("artist_id_list.csv", "r",newline='',encoding='gb18030') as csvfile:
#, encoding="utf-8"
        reader = csv.reader(csvfile)
        for row in reader:
            artist_id, artist_name = row
            if str(artist_id) is "artist_id":
                continue
            else:
                yield artist_id, artist_name
    # 当程序的控制流程离开with语句块后, 文件将自动关闭
#Body
headers={"cache-control":"no-cache",
         "Postman-Token":"f1645244-1df5-43a9-b379-ac4a7fe37d01",
         "User-Agent":"PostmanRuntime/7.4.0",
         "Accept":"*/*",
         "Host":"music.163.com",
         "accept-encoding":"gzip, deflate",
         "Connection":"keep-alive"}

#获取嵌套字典中的值
def dict_get(dict, objkey, default):
    tmp = dict
    for k,v in tmp.items():
        if k == objkey:
            return v
        else:
            if type(v) is dict:
                ret = dict_get(v, objkey, default)
                if ret is not default:
                    return ret
    return default

#请求地址
#urlwyy="http://music.163.com/api/artist/"+artistid
songlistid=469605931
#for readcsv in read_csv():
    #artist_id, artist_name = readcsv
url = "http://music.163.com/api/playlist/detail?id=" + str(songlistid)
    #建立连接
    #print("链接:"+url)
r=requests.get(url,headers=headers)
    #print("正在建立连接...")
gd = r.json()
info=gd['result']
    #if ret1 is not None:
print(info['id'],info['userId'],info['name'],info['tags'],info['trackCount'],info['createTime'],info['description'],info['commentThreadId'],info['coverImgUrl'])
        #print (ret1,"  ",ret2,"\n",ret3)
tags="".join(info['tags'])
sql = "insert into songlist(songlist_id,user_id,songlist_name,songlist_label,song_number,songlist_time,description,commentThread,imgUrl) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cursor.execute(sql,[info['id'],
               info['userId'],
               info['name'],
               tags,
               info['trackCount'],
               info['createTime'],
               info['description'],
               info['commentThreadId'],
               info['coverImgUrl']])  # 列表格式数据'''
conn.commit()   # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
print("数据上传结束")
cursor.close()  # 关闭游标
conn.close()  # 关闭连接
