from os import listdir, rename
from re import findall


def read_file_name(_path):
    _files = listdir(_path)
    for _file in _files:
        old_file_name = f"{_path}/{_file}"
        old_num = "".join(findall(r"\d", old_file_name))
        new_num = old_num.zfill(3)
        new_file_name = f"{_path}/{_file}".replace(old_num, new_num)
        print(new_file_name.split("/")[-1])
        rename(old_file_name, new_file_name)


if __name__ == "__main__":
    path = r"D:\内科（压缩）"
    read_file_name(path)
