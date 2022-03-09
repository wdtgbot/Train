import base64
import os
import time

import requests


def get_images(_path):
    _lists = os.listdir(_path)
    _lists.sort(key=lambda fn: os.path.getmtime(_path + "\\" + fn))
    _file = os.path.join(_path, _lists[-1])
    if _file.endswith(".jpg") or _file.endswith(".png"):
        with open(_file, "rb") as _f:
            _context = _f.read()
        return base64.b64encode(_context), _file
    else:
        print("同级目录下最新的文件类型并非为JPG或PNG！")
        return False, None


def get_token(_client_id, _client_secret):
    _url = "https://aip.baidubce.com/oauth/2.0/token"
    _params = {
        "grant_type": "client_credentials",
        "client_id": _client_id,
        "client_secret": _client_secret
    }
    _response = requests.get(_url, params=_params).json()
    if _response:
        return _response['access_token']
    else:
        print("获取access_token失败！")
        return False


def get_words(_access_token, _image, _file):
    _path = "\\".join(_file.split("\\")[:-1])
    _name = _file.split("\\")[-1]
    _url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    _url = f"{_url}?access_token={_access_token}"
    _headers = {'content-type': 'application/x-www-form-urlencoded'}
    _data, _text = {"image": _image, "detect_direction": "true"}, ""
    _response = requests.post(_url, headers=_headers, data=_data).json()
    for _word in _response['words_result']:
        with open(f"{_path}\\{_name.split('.')[0]}.txt", "a", encoding="utf-8") as _f:
            _f.write(_word['words'] + "\n")
        _text += _word['words']
    with open(f"{_path}\\{_name.split('.')[0]}.txt", "a", encoding="utf-8") as _f:
        _f.write("\n" + _text)
    print(f"已经将识别后的全文写入{_path}\\{_name.split('.')[0]}.txt")
    print(f"识别后的全文如下：\n\n{_text}")
    if input(f"\n\n是否需要删除{_name}文件？是：1 否：任意键") == "1":
        os.remove(_file)
        
    
if __name__ == '__main__':
    API_KEY = "mdlipqYgwT2hD4TG5qnSCBTl"
    SECRET_KEY = "dhTdswsgrHwT1BrU3wyWb8omFFT6kNDv"
    image, file = get_images(os.getcwd())
    if image:
        access_token = get_token(API_KEY, SECRET_KEY)
        if access_token:
            get_words(access_token, image, file)
    for _num in range(10):
        print(f"\r程序将在{10 - _num}秒后退出", end="")
        time.sleep(1)
            