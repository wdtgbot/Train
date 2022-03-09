from requests import get
from urllib.parse import unquote


def geocoding():
    url = "https://api.map.baidu.com/geocoding/v3/"
    data = {
        "address": unquote(location),
        "output": "json",
        "ak": ak
    }
    res = get(url=url, params=data).json()['result']['location']
    print("纬度：", res['lat'])
    print("经度：", res['lng'])


if __name__ == "__main__":
    location = "广东省佛山市三水区云山北路"
    ak = ""
    geocoding()
