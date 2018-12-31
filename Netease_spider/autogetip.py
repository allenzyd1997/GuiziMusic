from selenium import webdriver
import pymysql


driver=webdriver.Chrome()
driver.get('http://www.xicidaili.com/')

ip=driver.find_elements_by_xpath('//*[@id="ip_list"]/tbody/tr/td[2]')
ip=[i.text for i in ip]

port=driver.find_elements_by_xpath('//*[@id="ip_list"]/tbody/tr/td[3]')
port=[i.text for i in port]

type=driver.find_elements_by_xpath('//*[@id="ip_list"]/tbody/tr/td[6]')
type=[i.text for i in type]


conn = pymysql.connect(host = "localhost", port = 3306, user = "root", password = "root", db = "gz_musicdb", charset = "utf8")
sql='insert into ipcontent(ip,port,type) values(%s,%s,%s)'
cursor = conn.cursor()
for i in range(len(ip)):
    print('正在插入地{}条'.format(i))
    cursor.execute(sql, (ip[i],port[i],type[i]))
conn.commit()
cursor.close()
conn.close()