from requests import get


def geocoding():
    url = "https://api.map.baidu.com/reverse_geocoding/v3/"
    data = {
        "ak": ak,
        "output": "json",
        "location": location,
        "extensions_town": "true"
    }
    res = get(url=url, params=data).json()
    print(res)
    print("省份：", res['result']['addressComponent']['province'])
    print("城市：", res['result']['addressComponent']['city'])
    print("行政区：", res['result']['addressComponent']['district'])
    print("街道：", res['result']['addressComponent']['town'])
    print("路段：", res['result']['addressComponent']['street'])
    print("编码：", res['result']['addressComponent']['adcode'])
    print("纬度：", res['result']['location']['lat'])
    print("经度：", res['result']['location']['lng'])


if __name__ == "__main__":
    location = "23.21530592654246,112.86000113288719"
    ak = ""
    geocoding()
