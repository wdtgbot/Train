import json
import requests
from lxml import etree
from datetime import datetime


def main():
    url = "http://cas.shutcm.edu.cn/cas/login?service=http%3A%2F%2Fwork.shutcm.edu.cn%2Fyqtb%2Findex.jsp%3FdomainId%3D1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
    tree = etree.HTML(session.get(url, headers=headers).text)
    hidden = tree.xpath('//*[@id="fm1"]/div/p[3]/input[1]/@value')[0]
    data = {"username": username, "password": password, "_eventId": "submit", "loginType": "1", "submit": "登 录", "execution": hidden}
    session.post(url, headers=headers, data=data)
    url = "http://work.shutcm.edu.cn/yqtb/_web/_apps/poe/mrdk/dk_szy.jsp?menuId=23&domainId=1"
    session.get(url, headers=headers)
    url = "http://work.shutcm.edu.cn/yqtb/_web/_apps/poe/mrdk/api/add.rst?domainId=1"
    data = {"dktw": "36.3℃~37.3℃", "jkzt": "201", "qzbl": "否", "ysbl": "否", "szdlx": szdlx, "szddz": szddz, "xq": szddz.split("-")[0], "ly": szddz.split("-")[1], "fjh": szddz.split("-")[2], "szd_province": szdsqh.split("-")[0], "szd_city": szdsqh.split("-")[1], "szd_county": szdsqh.split("-")[2], "zxjzgc": "0", "sfks": "0", "qtrzt": "否", "qtrbqzt": "否", "glgczt": "否", "glts": "", "fhtz": "否", "sfzgfxdqfh": "0", "crjx": "否", "agree": "1", "xcxx": "[]", "szdsqh": szdsqh, "szdfxdj": "0", "szd": szddz}
    res = session.post(url, headers=headers, data=data).json()
    print(res)


def push(res):
    if token:
        url = 'http://www.pushplus.plus/send'
        data = {'token': token, 'title': "今日打卡情况", 'content': res, 'template': "text"}
        requests.post(url, data=data)


if __name__ == "__main__":
    now = datetime.now()
    session = requests.session()
    with open('./config.json', 'r', encoding='utf-8') as f:
        users = json.load(f)
    print(f'共需要签到{len(users)}人！')
    for i in range(len(users)):
        username = users[i]['username']
        password = users[i]['password']
        szdlx = users[i]['szdlx']
        szddz = users[i]['szddz']
        szdsqh = users[i]['szdsqh']
        token = users[i]['token']
    main()
    print('\n运行耗时：', datetime.now() - now)
