import requests


def jwsession(_u, _p, _s):
    url = "https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username"
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {
        "username": _u,
        "password": _p
    }
    data = "{}"
    response = requests.post(url, headers=headers, params=params, data=data)
    response_json = response.json()
    if response_json['code'] == 0:  # 成功！
        print(response.headers['JWSESSION'])
    else:
        print(response_json)
        # {'code': 101, 'message': '用户名或密码错误,还可再试4次'}
        return
    headers['JWSESSION'] = response.headers['JWSESSION']
    if _s:
        url = "https://student.wozaixiaoyuan.com/heat/getTodayHeatList.json"
        response = requests.post(url, headers=headers)
        response_json = response.json()
        print(response_json)
        # {'code': 0, 'data': [{'endTime': '10:00', 'seq': 1, 'startTime': '07:00', 'state': 0, 'type': 0}, {'endTime': '15:00', 'seq': 2, 'startTime': '12:00', 'state': 0, 'type': 0}, {'endTime': '23:00', 'seq': 3, 'startTime': '22:00', 'state': 0, 'type': 0}]}
    else:
        url = "https://student.wozaixiaoyuan.com/health/getHealthLatest.json"
        response = requests.post(url, headers=headers)
        response_json = response.json()
        print(response_json)
        
    
if __name__ == "__main__":
    jwsession("15283119690", "zkx1111swl.", True)
    