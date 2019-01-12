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
'''
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
headers = {"Proxy-Tunnel": str(tunnel)}'''


#连接数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='gz_musicdb', charset='utf8')
cursor=conn.cursor()
#存数据到数据库

#Body
headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
         'Accept-Encoding': 'gzip, deflate',
         'Accept-Language': 'zh-CN,zh;q=0.9',
         'Connection': 'keep-alive',
         'Cookie': 'WM_TID=36fj4OhQ7NdU9DhsEbdKFbVmy9tNk1KM; _iuqxldmzr_=32; _ntes_nnid=26fc3120577a92f179a3743269d8d0d9,1536048184013; _ntes_nuid=26fc3120577a92f179a3743269d8d0d9; __utmc=94650624; __utmz=94650624.1536199016.26.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); WM_NI=2Uy%2FbtqzhAuF6WR544z5u96yPa%2BfNHlrtTBCGhkg7oAHeZje7SJiXAoA5YNCbyP6gcJ5NYTs5IAJHQBjiFt561sfsS5Xg%2BvZx1OW9mPzJ49pU7Voono9gXq9H0RpP5HTclE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed5cb8085b2ab83ee7b87ac8c87cb60f78da2dac5439b9ca4b1d621f3e900b4b82af0fea7c3b92af28bb7d0e180b3a6a8a2f84ef6899ed6b740baebbbdab57394bfe587cd44b0aebcb5c14985b8a588b6658398abbbe96ff58d868adb4bad9ffbbacd49a2a7a0d7e6698aeb82bad779f7978fabcb5b82b6a7a7f73ff6efbd87f259f788a9ccf552bcef81b8bc6794a686d5bc7c97e99a90ee66ade7a9b9f4338cf09e91d33f8c8cad8dc837e2a3; JSESSIONID-WYYY=G%5CSvabx1X1F0JTg8HK5Z%2BIATVQdgwh77oo%2BDOXuG2CpwvoKPnNTKOGH91AkCHVdm0t6XKQEEnAFP%2BQ35cF49Y%2BAviwQKVN04%2B6ZbeKc2tNOeeC5vfTZ4Cme%2BwZVk7zGkwHJbfjgp1J9Y30o1fMKHOE5rxyhwQw%2B%5CDH6Md%5CpJZAAh2xkZ%3A1536204296617; __utma=94650624.1052021654.1536048185.1536199016.1536203113.27; __utmb=94650624.12.10.1536203113',
         'Host': 'music.163.com',
         'Referer': 'http://music.163.com/',
         'Upgrade-Insecure-Requests': '1',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/66.0.3359.181 Safari/537.36'}

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
        

#读取文件
count=0
sql="select album_id from songinfo"
df=pd.read_sql(sql=sql,con=conn)
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
    #print(gd)
    try:
        info=gd['album']
        albumname=info['name']
        singerid=info['artist']['id']
        date=info['publishTime']
        label=info['tags']
        picurl=info['picUrl']
        commentThread=info['info']['commentThread']['id']
        size=info['size']
        print(albumid,"/",albumname,"/",singerid,"/",date,"/",label,"/",picurl,"/",commentThread)

        #break
    except:
        with open('getalbuminfo_log.txt','a+',encoding='utf8') as f:
            f.write("读取返回json值gd出错："+albumid+"\n")
            continue
    print("第",count,"个专辑信息正在导入：")
    try:
        sql = "insert into albuminfo(album_id,album_name,singer_id,album_date,album_pic,commentThread,size) values(%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, [str(albumid),albumname,singerid,date,picurl,commentThread,size])  # 列表格式数据
        conn.commit()   # 提交，不然无法保存插入或者修改的数据(这个一定不要忘记加上)
    except Exception as e:
        print("插入专辑信息失败",e)
    else:
        print("                                                     上传成功")
    #break
print("数据上传结束")
cursor.close()  # 关闭游标
conn.close()  # 关闭连接
