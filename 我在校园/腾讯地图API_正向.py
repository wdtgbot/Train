from requests import get
from urllib.parse import unquote


def geocoding():
    url = "https://apis.map.qq.com/ws/geocoder/v1/"
    data = {
        "address": unquote(location),
        "key": key
    }
    res = get(url=url, params=data).json()['result']['location']
    print("纬度：", res['lat'])
    print("经度：", res['lng'])


if __name__ == "__main__":
    location = "广东省佛山市三水区广东财经大学"
    key = ""
    geocoding()
