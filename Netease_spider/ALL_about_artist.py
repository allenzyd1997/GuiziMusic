#-*-coding:utf-8-*- 
import requests
import csv
import pandas as pd
import json
import time

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
#params={'id':'2533973259'}
'''headers={"Cookies":"appver=1.5.0.75771;",
         "Refer":"http://music.163.com/"}'''

headers={"Cookie": "appver=1.5.0.75771;",
         "Referer": "http://music.163.com/",
         "cache-control":"no-cache",
         "Postman-Token":"02a1cb25-d7bb-437e-a13b-47f9f4cc8749",
         "User-Agent":"PostmanRuntime/7.4.0",
         "Accept":"*/*",
         "Host":"music.163.com",
         "accept-encoding":"gzip, deflate",
         "Connection":"keep-alive"}

#请求地址
#urlwyy="http://music.163.com/api/artist/"+artistid

for readcsv in read_csv():
    artist_id, artist_name = readcsv
    url = "http://music.163.com/api/artist/" + str(artist_id)
    #建立连接
    r=requests.get(url,headers=headers)
    print("正在建立连接...")
    gd = r.json()
    print(gd)
    print(json.dumps(gd, sort_keys=True, indent=2))
    time.sleep(20)
    print("将信息转存至文件...")
    pd.DataFrame(gd,index=[0]).to_csv(artist_name+'_info.csv')
    #print (get_dict_value(gd,result.tracks.name))
