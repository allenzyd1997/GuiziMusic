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
proxyUser = "16KKHDSD"
proxyPass = "759940"

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

def data_get(url):
    try:
        r=requests.get(url,headers=headers)
        r.encoding = "utf-8"
        if r.status_code == 200:
            return r.json()
        else:
            return 0
    except:
        print("查询专辑信息出错")
        return 0

#连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='gz_musicdb', charset='utf8')
cursor=conn.cursor()


sql="select album_id from albuminfo"
df=pd.read_sql(sql=sql,con=conn)

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


    #请求地址
    lines=df.shape[0]
    count=0
    for items in df.values:
        count=count+1
        albumid=items[0]
        url = "http://music.163.com/api/album/" + str(albumid) + "?id=" + str(albumid)
        #建立连接
        gd=data_get(url)
        if gd==0:
            with open('getalbuminfo_log.txt','a+',encoding='utf8') as f:
                f.write("专辑:"+albumid+"请求失败"+"\n")
                print("专辑:"+albumid+"请求失败"+"\n")
            continue
        else:
            print("开始爬取第",count,"个专辑")
        try:
            info=gd['album']
            songinfo=info['songs']
            order=-1
            for song in songinfo:
                order=order+1
                basicinfo=songinfo[order]
                songid=basicinfo['id']
                songname=basicinfo['name']
                singerid=info['artist']['id']
                duration=basicinfo['duration']
                popularity=basicinfo['popularity']
                playurl="https://api.bzqll.com/music/netease/url?key=579621905&id="+str(songid)
                picurl="https://api.bzqll.com/music/netease/pic?key=579621905&id="+str(songid)
                lrcurl="https://api.bzqll.com/music/netease/lrc?key=579621905&id="+str(songid)
                commentThread="R_SO_4_"+str(songid)
                try:
                    sql = "insert into songinfo(song_id,song_name,singer_id,album_id,song_url,pic_url,lrc_url,duration,popularity,commentThread) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql,[str(songid),songname,singerid,str(albumid),playurl,picurl,lrcurl,duration,popularity,commentThread])  # 列表格式数据
                    conn.commit()   # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
                except Exception as e:
                    print("录入数据库失败!可能出现重复数据",e)
                    continue
                else:
                    print("第",count,"张专辑第",order+1,"首歌曲："+songname+"信息上传成功！")
        except Exception as e:
            print("json中读取数据失败：",e)
            with open ('专辑出错.json','w',encoding='utf8') as f:
                f.write(json.dumps(gd,ensure_ascii=False,indent=2))
                f.close()
            break
            #continue
    print("数据上传结束")
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接