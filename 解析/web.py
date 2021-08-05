# -*- coding: utf-8 -*-
# Time     :  2021/7/20 21:53
# Author   :  老飞机
# File     :  web.py
# Software :  PyCharm
import re
import base64
import requests
from flask import *

app = Flask(__name__)
app.config.update(DEBUG=True)


@app.route("/",methods=['GET' ])
def index():
    return render_template('index.html')


@app.route("/play",methods=['GET' , "POST"])
def play():
    print((request.form))
    return render_template('play.html')


@app.route("/iqy",methods=['GET' , "POST"])
def tx():
    url = base64.b64decode(bytes(request.args.get("url") , "utf-8")).decode()
    try:
        response = requests.get(url , headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}).text
        albumId = re.findall("""param\['albumid'\] = "(.*?)\"""" , response)[0]
    except:
        albumId = ""
    return '''{"data" : {"videos" : [{"lfj_albumId" : "%s"}]}}'''%albumId




if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8889,
    )
