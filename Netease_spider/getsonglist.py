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

#连接数据库
#conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='gz_musicdb', charset='utf8')
#cursor=conn.cursor()
#存数据到数据库


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
for readcsv in read_csv():
    songlistid = 912256078
    print("//",songlistid,"//")
    #songlistid=''.join(songlistid)
    print("//",songlistid,"//")
    url = "http://music.163.com/api/playlist/detail?id=" + str(songlistid)
    try:
        r=requests.get(url,headers=headers)
        gd = r.json()
        if r.status_code==200:
            #print(gd)
            info=gd['result']
            #print(info)

        else:
            print(songlistid,"请求出错",r.status_code)
            with open('getsonglist_log.txt','a+',encoding='utf8') as f:
                f.write("内容出错："+str(songlistid)+"\n")
            continue  
    except Exception as e:
        print("请求失败",e)
        with open('getsonglist_log.txt','a+',encoding='utf8') as f:
                f.write("请求失败："+str(songlistid)+"\n")
        continue
        #if ret1 is not None:
    #print(info['id'],info['userId'],info['name'],info['tags'],info['trackCount'],info['createTime'],info['description'],info['commentThreadId'],info['coverImgUrl'])
    tags="".join(info['tags'])
    '''try:
        sql = "insert into songlist(songlist_id,user_id,songlist_name,songlist_label,song_number,songlist_time,description,commentThread,imgUrl) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,[info['id'],
                    info['userId'],
                    info['name'],
                    tags,
                    info['trackCount'],
                    info['createTime'],
                    info['description'],
                    info['commentThreadId'],
                    info['coverImgUrl']])  # 列表格式数据
        conn.commit()   # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
    except Exception as e:
        print("歌单存入失败，可能出现重复",e)'''
    slistinfo=str(info['name'])+"##"+str(tags)+"##"+str(info['id'])+"##"+str(info["shareCount"])
    print(slistinfo,end=" ")
    tracks=info['tracks']
    #print(tracks)
    for track in tracks:
        #print(track)
        artist=track['artists'][0]
        trackinfo=str(track['id'])+"::"+str(track['name'])+"::"+str(artist['name'])+"::"+str(track['popularity'])
        print(trackinfo,end=" ")
    break
print("数据上传结束")
#cursor.close()  # 关闭游标
#conn.close()  # 关闭连接
