# coding = utf-8

import sys
import json
import base64
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode


def fetch_token():
    result_str = None
    params = {
        'grant_type': 'client_credentials',
        'client_id': API_KEY,
        'client_secret': SECRET_KEY
    }
    post_data = urlencode(params)
    if IS_PY3:
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    if IS_PY3:
        result_str = result_str.decode()
    res = json.loads(result_str)
    if 'access_token' in res.keys() and 'scope' in res.keys():
        if 'brain_all_scope' not in res['scope'].split(' '):
            print('please ensure has check the  ability')
            exit()
        return res['access_token']
    else:
        print('please overwrite the correct API_KEY and SECRET_KEY')
        exit()


def read_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        return f.read()
    except Exception as e:
        print('read image file fail')
        print(e)
        return None
    finally:
        if f:
            f.close()


def request(url, data):
    req = Request(url, data.encode('utf-8'))
    try:
        f = urlopen(req)
        result_str = f.read()
        if IS_PY3:
            result_str = result_str.decode()
        return result_str
    except URLError as err:
        print(err)


if __name__ == '__main__':
    API_KEY = ''
    SECRET_KEY = ''
    OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_analysis_office"
    TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'
    token = fetch_token()
    image_url = OCR_URL + "?access_token=" + token
    text = ""
    file_content = read_file('./text.jpg')
    result = request(image_url, urlencode({'image': base64.b64encode(file_content)}))
    result_json = json.loads(result)
    # i = 0
    for word in result_json['results']:
        string = word['words']['word']
        print(string)
    # print(i)
