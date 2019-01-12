import requests,os,json,base64
from scrapy.selector import Selector
from  binascii import hexlify
from Crypto.Cipher import AES
from urllib.request import urlretrieve
import flask
from flask import request  #获取参数
import json
import sys

'''server = flask.Flask(__name__) #创建一个flask对象
@server.route('/download', methods=['get','post'])'''

class Encrypyed():
    '''传入歌曲的ID，加密生成'params'、'encSecKey 返回'''
    def __init__(self):
        self.pub_key = '010001'
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'

    def create_secret_key(self, size):
        return hexlify(os.urandom(size))[:16].decode('utf-8')

    def aes_encrypt(self,text, key):
        iv = '0102030405060708'
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        encryptor = AES.new(bytes(key, encoding = "utf8"), AES.MODE_CBC, bytes(iv, encoding = "utf8"))
        result = encryptor.encrypt(bytes(text, encoding = "utf8"))
        result_str = base64.b64encode(result).decode('utf-8')
        return result_str

    def rsa_encrpt(self,text, pubKey, modulus):
        text = text[::-1]
        rs = pow(int(hexlify(text.encode('utf-8')), 16), int(pubKey, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)

    def work(self,text):
        text = json.dumps(text)
        i=self.create_secret_key(16)
        encText =self.aes_encrypt(text, self.nonce)
        encText=self.aes_encrypt(encText,i)
        encSecKey=self.rsa_encrpt(i,self.pub_key,self.modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data


class wangyiyun():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Referer': 'http://music.163.com/'}
        self.main_url='http://music.163.com/'
        self.session = requests.Session()
        self.session.headers=self.headers
        self.ep=Encrypyed()

    def get_songurls(self,playlist):
        '''进入所选歌单页面，得出歌单里每首歌各自的ID 形式就是“song?id=64006"'''
        url=self.main_url+'playlist?id=%d'% playlist
        re= self.session.get(url)   #直接用session进入网页，懒得构造了
        sel=Selector(text=re.text)   #用scrapy的Selector，懒得用BS4了
        songurls=sel.xpath('//ul[@class="f-hide"]/li/a/@href').extract()
        return songurls   #所有歌曲组成的list
        ##['/song?id=64006', '/song?id=63959', '/song?id=25642714', '/song?id=63914', '/song?id=4878122', '/song?id=63650']


    def get_songinfo(self,songurl):
        '''根据songid进入每首歌信息的网址，得到歌曲的信息
        return：'64006'，'陈小春-失恋王'''
        url=self.main_url+songurl
        re=self.session.get(url)
        sel=Selector(text=re.text)
        song_id = url.split('=')[1]
        song_name = sel.xpath("//em[@class='f-ff2']/text()").extract_first()
        singer= '&'.join(sel.xpath("//p[@class='des s-fc4']/span/a/text()").extract())
        songname=singer+'-'+song_name
        return str(song_id),songname

    def get_url(self,ids,br=128000):
        '''self.ep.work输入歌曲ID，解码后返回data，{params 'encSecKey}
        然后post，得出歌曲所在url'''
        text = {'ids': [ids], 'br': br, 'csrf_token': ''}
        data=self.ep.work(text)
        url = 'http://music.163.com/weapi/song/enhance/player/url?csrf_token='
        req = self.session.post(url, data=data)
        song_url=req.json()['data'][0]['url']
        #print(song_url)
        return song_url

    def download_song(self, songurl, dir_path):
        '''根据歌曲url，下载mp3文件'''
        song_id, songname = self.get_songinfo(songurl) #根据歌曲url得出ID、歌名
        #print("songid=",song_id)
        song_url = self.get_url(song_id)                #根据ID得到歌曲的实质URL
        path = dir_path + '\\' + songname + '.mp3'   #文件路径
        #print(song_url)
        return song_url
        #urlretrieve(song_url, path)            #下载文件

    def work(self,playlist):
        songurls=self.get_songurls(playlist)         #输入歌单编号，得到歌单所有歌曲的url
        dir_path=r'D:\GuiziMusicDld'
        for songurl in songurls:
            self.download_song(songurl,dir_path)
            #print(songurl)     #下载歌曲

'''def download():
    songid=request.values.get('songid')
    d=wangyiyun()
    dldurl=d.get_url(songid)
    print(dldurl)
    #song_url=json.dump(dldurl)
    return song_url'''
    
#server.run(port=8080,debug=True)

def main():
    d=wangyiyun()
    inputid=sys.argv[1]
    url=d.get_url(inputid)
    print(url,end='')
    #return url

if __name__ == '__main__':
   main()