#-*-coding:utf-8-*- 
import requests
import csv
import pandas as pd
import json
import time
import types
import pymysql
import codecs
import time

from bs4 import BeautifulSoup
import requests
import random
import urllib.request


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


def read_csv():

    with open("songs.csv", "r",newline='',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            songid = row
            if str(songid) is "song_id":
                continue
            else:
                yield songid

#连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='gz_musicdb', charset='utf8')
cursor=conn.cursor()

#Body
headers={"cache-control":"no-cache",
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
         'Accept-Encoding': 'gzip, deflate',
         "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.181 Safari/537.36',
         "Host":"music.163.com",
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


if __name__ == '__main__':
    count=0
    for readcsv in read_csv():
        songids = readcsv
        songids=''.join(songids)
        print("id",songids)
        #请求地址
        count+=1
        print("第",count,"首歌")
        url1 = "http://music.163.com/api/song/detail/?id="+str(songids)+"&ids=%5B"+str(songids)+"%5D"    #建立连接
        #url2 = "https://api.bzqll.com/music/netease/song?key=579621905&id="+str(items[0])
        try:
            r=requests.get(url1,proxies=proxies,headers=headers,timeout=4)
            gd = r.json()#json存入字典
            songinfo=gd['songs'][0]
        except Exception as e:
            sid=songids
            print(str(sid),"该歌曲出现错误！！请检查！！",e)
            try:
                sql="insert into reload(song_id,reloadtimes) values(%s,%s);"
                cursor.execute(sql,[str(sid),'0'])
                conn.commit()
            except Exception as e:
                #stimes+=1
                print("reload表中已有歌曲",str(sid),e)
                sql="update reload set song_id=%s,reloadtimes=3 where song_id=%s"
                cursor.execute(sql,[str(sid),str(sid)])
                conn.commit()
                time.sleep(1)
                continue
            continue
        #print("This is LEngth of sons", len(gd['songs']))
        
        
        artistinfo=songinfo['artists'][0]
        albuminfo=songinfo['album']
        songid=songids
        songname=songinfo['name']
        singerid=artistinfo['id']
        duration=songinfo['duration']
        popularity=songinfo['popularity']
        commentThread=songinfo['commentThreadId']
        playurl="https://api.bzqll.com/music/netease/url?key=579621905&id="+str(songids)
        picurl="https://api.bzqll.com/music/netease/pic?key=579621905&id="+str(songids)
        lrcurl="https://api.bzqll.com/music/netease/lrc?key=579621905&id="+str(songids)
        album=albuminfo['id']
        try:
            sql = "insert into songinfo(song_id,song_name,singer_id,album_id,song_url,pic_url,lrc_url,duration,popularity,commentThread) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,[songid,songname,singerid,album,playurl,picurl,lrcurl,duration,popularity,commentThread])  # 列表格式数据'''
            conn.commit()   # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
        except Exception as e:
            print(songid,songname,"录入数据库失败!可能出现重复数据",e)
            continue
    print("数据上传结束")
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接