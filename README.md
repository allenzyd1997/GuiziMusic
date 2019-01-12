GuiziMusic音乐平台子系统——爬虫部分
---
[<img alt="GuiziMusic" src="https://github.com/allenzyd1997/GuiziMusic/blob/master/src/common/image/logo.png" width="250">](https://github.com/allenzyd1997/GuiziMusic)

**主要制作人员：Jackyliu**

灵感来自
---
>[zyingzhou](https://github.com/zyingzhou)/**[music163-spiders](https://github.com/zyingzhou/music163-spiders)**
 
>[Binaryify](https://github.com/Binaryify)/**[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)**

环境要求
---

python3.x

使用的库主要有requests,csv,pandas,json,pymysql,codecs,安装比较麻烦的有pycrypto(可用pycryptodome代替)
MySQL数据库



文件功能说明
---
+ **16yun.py**        
>*使用的亿牛云ip代理，其他程序设置代理时参考用*
+ **download.py**
>*歌曲下载实现模块，可通过python download.py 'songid'的命令行形式调用下载*
+ **downloadapi.py** 
>*歌曲下载接口，使用flask包装接口，运行后在浏览器以localhost:8000/download?songid='songid'的形式获取下载音乐的地址*
+ **getartist.py** 
>*歌手列表爬虫，使用bs4在网易云的歌手列表页面爬取歌手id，姓名和分类*
+ **getcomments.py**
>*歌曲评论爬虫，需要配合歌曲的csv文件使用，读取csv中的歌曲id，通过AES加密和RSA加密获取请求评论所需的params和encSecKey，然后将评论数据和用户数据存入数据库*
+ **get_hot_songs.py** 
>*歌手热门歌曲爬虫，使用的selenium方法模拟浏览器行为来获取歌手的热门歌曲，本次项目没有使用，可供参考*
+ **get_lyric.py** 
>*歌词爬虫，和评论类似，AES和RSA加密获得歌词url，本项目中使用其他接口获得歌词，可供参考*
+ **getalbum.py**
>*专辑爬虫，需和歌曲数据库搭配使用，将getsonginfo.py存入songinfo表中的albumid取出并请求对应专辑的信息，存入albuminfo表中*
+ **getalbumcmt,py** 
>*专辑评论爬虫，和歌曲评论爬虫相似，但需要数据库albuminfo中的albumid字段来确定爬哪个专辑*
+ **getartistinfo.py** 
>*歌手信息爬虫，读取getartist.py导出的歌手列表csv文件，请求相应歌手信息，并存入数据库artistinfo表*
+ **getsonginfo.py**
>*歌曲信息爬虫，读取songlist_relation表中所有歌曲id，请求歌曲信息并存入songinfo表中*
+ **getsonginfo(fromcsv).py**
>*歌曲信息爬虫，同上，仅将获取数据的来源改为csv文件，数据量较大时方便多进程获取歌曲信息*
+ **getsonglist.py**
>*歌单爬虫，修改中，可通过输入歌单id来获取歌单信息并存入songlist表中*
+ **getsonglist(relation).py**
>*存储歌单歌曲关系，通过歌单id获取歌单包含的歌曲id并将歌单id和对应歌曲id存入songlist_relation表中形成映射关系*
+ **getsonglistcmt.py**
>*歌单评论爬虫我，和歌曲评论爬虫相似，需要表songlist中songlistid来确定爬的歌单*
+ **reloadsong.py**
>*随手写的重新载入歌曲信息的方法，使用代理并且歌曲数据量较大时请求出错会增多，因此设计了这样一个方法来重新录入之前请求失败的歌曲，需要reload表，未完善*
+ **songbyalbum.py**
>*根据专辑来获取歌曲的爬虫，基本功能和歌曲爬虫大致相同*
+ **sql2csv.py**
>*将数据库信息导入csv文件用的工具，便于多进程时使用*
+ **userdump.py**
>*十万阴兵的账号密码2333，拿来模拟用户用的*



贡献者
---
[<img alt="JackyLiu47" src="https://avatars0.githubusercontent.com/u/37102431?s=460&v=4" width="80">](https://github.com/JackyLiu47)
[<img alt="allenzyd1997" src="https://avatars3.githubusercontent.com/u/41326130?s=60&v=4" width="80">](https://github.com/allenzyd1997)[<img alt="MasterOfTheLion" src="https://avatars0.githubusercontent.com/u/29800142?s=60&v=4" width="80">](https://github.com/MasterOfTheLion)[<img alt="sunseayuy" src="https://avatars3.githubusercontent.com/u/46275985?s=60&v=4" width="80">](https://github.com/sunseayuy)[<img alt="liangletian" src="https://avatars2.githubusercontent.com/u/32542510?s=460&v=4" width="80">](https://github.com/liang15278589600)
