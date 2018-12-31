# -*- coding: utf-8 -*-
"""
Date: 2018-12-29
Description: 网易云歌手热门歌曲
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pymysql

'''class Operate_SQL():
    def __get_conn(self):
        try:
            self.conn=pymysql.connect(host='127.0.0.1',user='root',password='root',port=3306,db='gz_musicdb',charset='utf-8')
        except pymysql.Error as e:
            print(e,'数据库连接失败')
    
    def __close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print(e,'数据库断开失败')'''

def parse_html_page(html):
    # 使用双引号会出现 Unresolve reference
    # pattern = '<span class="txt"><a href="/song?id=(\d*)"><b title="(.*?)">'
    # 这里是使用lxml解析器进行解析,lxml速度快,文档容错能力强,也能使用html5lib
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('span', 'txt')
    return items


'''
# 这里以获取薛之谦的热门歌曲为例
url = "https://music.163.com/#/artist?id=5781"
html = get_html_src(url)
'''


# 将获得的歌手的热门歌曲id和名字写入csv文件
def write_to_csv(items, artist_name):

    with open("music_163_songs.csv", "a",newline='',encoding='gb18030') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["歌手名字", artist_name])

        for item in items:
            writer.writerow([item.a['href'].replace('/song?id=', ''), item.b['title']])
        '''
            # 可视化显示
            print('歌曲id:', item.a['href'].replace('/song?id=', ''))
            song_name = item.b['title']
            print('歌曲名字:', song_name)
        '''
    csvfile.close()


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


def main():
    # 可以任意选择浏览器,前提是要配置好相关环境,更多请参考selenium官方文档
    driver = webdriver.Chrome()
    chromeOptions = webdriver.ChromeOptions()

    # 设置代理
    chromeOptions.add_argument("--proxy-server=http://119.101.113.58:9999")
    # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
    browser = webdriver.Chrome(chrome_options = chromeOptions)
    # 避免多次打开浏览器
    for readcsv in read_csv():
        artist_id, artist_name = readcsv
        url = "https://music.163.com/#/artist?id=" + str(artist_id)
        print("正在获取{}的热门歌曲...".format(artist_name))
        driver.get(url)
        # 切换成frame
        driver.switch_to_frame("g_iframe")
        # 休眠3秒,等待加载完成!
        time.sleep(3)
        html = driver.page_source
        items = parse_html_page(html)
        print("{}的热门歌曲获取完成!".format(artist_name))
        print("开始将{}的热门歌曲写入文件".format(artist_name))
        write_to_csv(items, artist_name)
        print("{}的热门歌曲写入到本地成功!".format(artist_name))


if __name__ == "__main__":
    main()
