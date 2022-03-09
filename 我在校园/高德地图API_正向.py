from requests import get
from urllib.parse import unquote


def geocoding():
    url = "https://restapi.amap.com/v3/geocode/geo"
    data = {
        "address": unquote(location),
        "key": key
    }
    res = get(url=url, params=data).json()
    print(res)
    res = res['geocodes'][0]['location'].split(",")
    print("纬度：", res[1])
    print("经度：", res[0])


if __name__ == "__main__":
    location = "广东省佛山市三水区云山北路"
    key = ""
    geocoding()
