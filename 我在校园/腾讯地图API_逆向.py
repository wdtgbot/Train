from requests import get


def geocoding():
    url = "https://apis.map.qq.com/ws/geocoder/v1/"
    data = {
        "key": key,
        "location": location
    }
    res = get(url=url, params=data).json()
    print(res)
    print("省份：", res['result']['address_component']['province'])
    print("城市：", res['result']['address_component']['city'])
    print("行政区：", res['result']['address_component']['district'])
    print("街道：", res['result']['address_reference']['town']['title'])
    print("路段：", res['result']['address_component']['street'])
    print("编码：", res['result']['ad_info']['adcode'])
    print("纬度：", res['result']['address_reference']['street']['location']['lat'])
    print("经度：", res['result']['address_reference']['street']['location']['lng'])


if __name__ == "__main__":
    location = "23.21247,112.86226"
    key = ""
    geocoding()
