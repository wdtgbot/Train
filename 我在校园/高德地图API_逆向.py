import requests


def geoCode():
    url = "https://restapi.amap.com/v3/geocode/regeo"
    data = {
        "location": location,
        "key": key
    }
    rego = requests.get(url=url, params=data).json()
    print(rego)
    print("省份：", rego['regeocode']['addressComponent']['province'])
    print("城市：", rego['regeocode']['addressComponent']['city'])
    print("行政区：", rego['regeocode']['addressComponent']['district'])
    print("街道：", rego['regeocode']['addressComponent']['township'])
    print("路段：", rego['regeocode']['addressComponent']['streetNumber']['street'])
    print("邮编：", rego['regeocode']['addressComponent']['adcode'])


if __name__ == "__main__":
    location = "110.943049,21.646782"
    key = ""
    geoCode()
