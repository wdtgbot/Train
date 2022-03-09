from requests import post


def main():
    url = f"https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username?username={username}&password={pwd}"
    headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 "}
    body = "{}"
    res = post(url, headers=headers, data=body)
    print(res.json())
    if res.json()['code'] == 0:
        print(res.headers['JWSESSION'])
    else:
        print(res.json()['message'])


if __name__ == "__main__":
    username = ""
    pwd = ""
    main()
