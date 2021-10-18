import requests
from hashlib import md5


def main(username, password, soft_id, codetype, image):
    base_params = {
        'user': username,
        'pass2': md5(password.encode('utf8')).hexdigest(),
        'softid': soft_id,
    }
    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
    }
    params = {
        'codetype': codetype,
    }
    params.update(base_params)
    files = {'userfile': ('ccc.jpg', image)}
    data = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=headers, proxies={"http": None, "https": None}).json()
    return data['pic_str']


if __name__ == "__main__":
    image = open('./code.jpg', 'rb').read()
    code = main("", "", "", "", image)
