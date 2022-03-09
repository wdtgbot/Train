# -*- coding: utf-8 -*-

from os import walk


def read_name(_dir):
    _lists = []
    for root, dirs, files in walk(_dir):
        if root == _dir:
            continue
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        _lists.append(root.split("\\")[-1])
    return _lists


if __name__ == "__main__":
    dir = r"D:\内科（压缩）"
    print(read_name(dir))
