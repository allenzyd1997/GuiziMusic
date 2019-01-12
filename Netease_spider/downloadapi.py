import flask
from flask import request  #获取参数
import json
import os
#import main from download as mymain

server = flask.Flask(__name__) #创建一个flask对象
@server.route('/download', methods=['get','post'])

def download():
    songid=request.values.get('songid')
    result=os.system("python download.py "+songid)
    resp=os.popen("python download.py "+songid).readlines()
    return str(resp)

server.run(port=8000,debug=True)