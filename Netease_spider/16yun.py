#! -*- encoding:utf-8 -*-
import requests
import random

# 要访问的目标页面
targetUrl = "http://httpbin.org/ip"

# 要访问的目标HTTPS页面
# targetUrl = "https://httpbin.org/ip"
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



resp = requests.get(targetUrl, proxies=proxies, headers=headers)

print(resp.status_code)
print(resp.text)