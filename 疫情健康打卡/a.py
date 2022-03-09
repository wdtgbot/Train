import requests
import urllib3
from uuid import uuid4
import time

urllib3.disable_warnings()

only_uuid = str(uuid4())

session = requests.session()

url = "https://e.kmmu.edu.cn/lyuapServer/login?service=https://xg.kmmu.edu.cn/SPCP/Web/"
print("1", url)
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.3"}
res = session.get(url, headers=headers, verify=False, allow_redirects=False)
res.encoding = "gdk"
print(res.status_code)

url = f"https://e.kmmu.edu.cn/lyuapServer/kaptcha?_t={int(time.time())}&uid="
print("2", url)
headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 yiban_iOS/4.9.3"}
res = session.get(url, headers=headers, verify=False, allow_redirects=False)
uid = res.json()['uid']
print(res.json()['content'])
print(uid)
