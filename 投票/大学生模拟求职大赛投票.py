from requests import session
from time import sleep, strftime, localtime
from datetime import datetime
from json import loads


def main(Cookie):
    url = "http://mnds.qcwyhr.com/web_admin/other/peopletickets.aspx?"
    data = "PeopleID=b8ccd3b773f04f7699da219d50b5fc0a&KindId=020506"
    headers = {
        'Host': 'mnds.qcwyhr.com',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://mnds.qcwyhr.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.14(0x18000e22) NetType/WIFI Language/zh_CN',
        'Connection': 'keep-alive',
        'Referer': 'http://mnds.qcwyhr.com/peoplelist.aspx',
        'Content-Length': '55',
        'Cookie': Cookie
    }
    i = 1
    while i:
        now = datetime.now()
        res = session.post(url, data=data, headers=headers)
        try:
            body = loads(res.text)
            if body['success']:
                print(f"{strftime('%H:%M:%S', localtime())}, {datetime.now() - now}, {body['success']}, {body['msg']}")
        except Exception as e:
            print(f"{strftime('%H:%M:%S', localtime())}, {e}, {res.text}")
            i = 0
        finally:
            sleep(3)


if __name__ == "__main__":
    session = session()
    while True:
        cookies = [
            ""
        ]
        for cookie in cookies:
            try:
                main(cookie)
            except Exception as error:
                print(f'{strftime("%H:%M:%S", localtime())} {error}')
                continue
                