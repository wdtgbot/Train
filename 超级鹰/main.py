import requests
import hashlib


def main(usn, pwd, soft_id, codetype, file):
    params = {'user': usn, 'pass2': hashlib.md5(pwd.encode('utf8')).hexdigest(), 'softid': soft_id, 'codetype': codetype}
    headers = {'Connection': 'Keep-Alive', 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'}
    files = {'userfile': ('code.jpg', open(file, 'rb').read())}
    data = requests.post('http://upload.chaojiying.net/Upload/Processing.php',
                         data=params, files=files, headers=headers, proxies={"http": None, "https": None}).json()
    return data['pic_str']


if __name__ == "__main__":
    code = main(
        "",
        "",
        "",
        "",
        "./code.jpg")
    # https://www.chaojiying.com/price.html
    print(code)
