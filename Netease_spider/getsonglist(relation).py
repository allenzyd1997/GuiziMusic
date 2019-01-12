#-*-coding:utf-8-*- 
import requests
import csv
import pandas as pd
import json
import time
import types
import pymysql
import codecs
import random

# 代理服务器
proxyHost = "b5.t.16yun.cn"
proxyPort = "6460"

# 代理隧道验证信息
proxyUser = "16GOFRKK"
proxyPass = "844515"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host" : proxyHost,
            "port" : proxyPort,
            "user" : proxyUser,
            "pass" : proxyPass,
}

# 设置 http和https访问都是用HTTP代理
proxies = {
    "http"  : proxyMeta,
    "https" : proxyMeta,
}


#  设置IP切换头
tunnel = random.randint(1,10000)
headers = {"Proxy-Tunnel": str(tunnel)}


#连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='gz_musicdb', charset='utf8')
cursor=conn.cursor()
#存数据到数据库


sqlr="select songlist_id from songlist_relation"
cursor.execute(sqlr)
data=cursor.fetchall()
#df=pd.DataFrame(data)#转换成DataFrame格式
#df.head()
if isinstance(data,dict):
        print("dict")
else:
    if isinstance(data,list):
        print("list")

# 获取歌单名
def read_csv():

    with open("popplaylist.csv", "r",newline='',encoding='utf-8') as csvfile:
#, encoding="utf-8"
        reader = csv.reader(csvfile)
        for row in reader:
            songlistid = row
            if str(songlistid) is "songlist_id":
                continue
            else:
                yield songlistid
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
count=0
for readcsv in read_csv():
    count+=1
    songlistid = readcsv
    #print("//",songlistid,"//")
    songlistid=''.join(songlistid)
    #print("//",songlistid,"//")
    url = "http://music.163.com/api/playlist/detail?id="+str(songlistid)+"&updateTime=-1"    #建立连接
        #print("链接:"+url)
    try:
        r=requests.get(url,proxies=proxies,headers=headers)
        #print("正在建立连接...")
        gd = r.json()#json存入字典
        if r.status_code==200:
            listinfo=gd['result']
        else:
            printf("请求结果出错")
            with open('SonglistRelation_log.txt','a+',encoding='utf8') as f:
                f.write("内容出错："+str(songlistid)+"\n")
            continue
    except Exception as e:
        print("请求失败",e)
        with open('SonglistRelation_log.txt','a+',encoding='utf8') as f:
                f.write("请求失败："+str(songlistid)+"\n")
        continue
    info=gd['result']['tracks']#解析字典
    print("第",count,"个歌单：")
    for items in info:
        songid=dict_get(items,'id',None)
        print(songid)
        try:
            sql = "insert into songlist_relation(songlist_id,song_id) values(%s,%s)"
            cursor.execute(sql,[listinfo['id'],songid])  # 列表格式数据'''
            conn.commit() 
        except Exception as e:
            print("数据上传出错！！",e)
            with open('SonglistRelation_log.txt','a+',encoding='utf8') as f:
                f.write("存储出错："+str(songid)+"\n")
        continue
print("数据上传结束")
cursor.close()  # 关闭游标
conn.close()  # 关闭连接
