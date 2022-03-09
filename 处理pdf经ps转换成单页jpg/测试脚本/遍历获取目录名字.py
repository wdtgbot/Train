# -*- coding: utf-8 -*-

import os


def file_name(file_dir):
    dir_lists = []
    for root, dirs, files in os.walk(file_dir):
        if root == file_dir:
            continue
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
        dir_lists.append(root.split("\\")[-1])
    print(dir_lists)
        
        
if __name__ == "__main__":
    dir = r"D:\内科（压缩）"
    file_name(dir)
    