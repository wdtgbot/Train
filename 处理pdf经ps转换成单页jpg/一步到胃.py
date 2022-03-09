from glob import glob
from os import listdir, walk, mkdir, rename
from shutil import copy, Error, rmtree
from time import sleep, perf_counter

from PIL import Image


def read_name(_dir):
    _lists = []
    for root, dirs, files in walk(_dir):
        if root == _dir:
            continue
        _lists.append(root.split("\\")[-1])
    return _lists


def squash_jpg(_init, _squash, _dir):
    i = 1
    _file_account = glob(f'{_init}/{dir}/*.jpg')
    _new_dir = f"{squash}/{dir}"
    try:
        mkdir(_new_dir)
    except FileExistsError:
        pass
    while i <= len(_file_account):
        img = Image.open(f'{_init}/{_dir}/{i}.jpg')
        img.save(f'{_new_dir}/{i}.jpg', quality=20)  # quality 为图片质量 100表示不压缩， 75表示压缩比例
        i = i + 1


def main(_squash, _dir, _num, _tar):
    _path = f"{_squash}/{_dir}"
    temp_dir = f"{_tar}/temporary"
    name = 0
    try:
        mkdir(temp_dir)
    except FileExistsError:
        pass
    _files = listdir(_path)
    _files.sort(key=lambda x: int(x.split(".")[0]))
    for _file in _files:
        old_file_path = f"{_path}/{_file}"
        copy(old_file_path, temp_dir)
    _files = listdir(temp_dir)
    scale = len(_files)
    _files.sort(key=lambda x: int(x.split(".")[0]))
    start = perf_counter()
    for _file in _files:
        old_file_path = f"{temp_dir}/{_file}"
        new_file_name = f"{temp_dir}/{name + _num}.jpg"
        rename(old_file_path, new_file_name)
        try:
            copy(new_file_name, _tar)
        except Error:
            pass
        a = "*" * (_files.index(_file) + 1)
        b = "." * (scale - (_files.index(_file)) - 1)
        c = ((_files.index(_file)) / scale) * 100
        dur = perf_counter() - start
        print(f"\r{_dir} {str(c)[:4]}% [{a}->{b}] {str(dur)[:5]}s {name + _num}", end="")
        name += 1
        sleep(0.1)
    rmtree(temp_dir)
    return _num + name


if __name__ == "__main__":
    num = 1
    subject = "内科"
    init = r"D:\xxx\原图".replace("xxx", subject)  # 原图路径
    squash = r"D:\xxx\压缩".replace("xxx", subject)  # 压缩后存放路径
    tar = r'D:\xxx\出书'.replace("xxx", subject)  # 移动到此目录保存图片
    try:
        mkdir(squash)
    except FileExistsError:
        pass
    try:
        mkdir(tar)
    except FileExistsError:
        pass
    print("执行开始".center(66, "-"))
    for dir in read_name(init):
        squash_jpg(init, squash, dir)
        num = main(squash, dir, num, tar)
    print("\n" + "执行结束".center(66, "-"))
