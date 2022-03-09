from os import listdir, mkdir, rename, rmdir
from shutil import copy, move


def main(_path, _num, _tar):
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
        # print(f"把{old_file_path}复制到{temp_dir}……")
        copy(old_file_path, temp_dir)
    _files = listdir(temp_dir)
    _files.sort(key=lambda x: int(x.split(".")[0]))
    for _file in _files:
        old_file_path = f"{temp_dir}/{_file}"
        new_file_name = f"{temp_dir}/{name + _num}.jpg"
        # print(f"把{old_file_path}重命名为{new_file_name}……")
        rename(old_file_path, new_file_name)
        # print(f"把{new_file_name}剪切到{_tar}……")
        move(new_file_name, _tar)
        name += 1
    rmdir(temp_dir)
    return _num + name


if __name__ == "__main__":
    init = r"D:\内科（原图）".replace("\\", "/")  # 原图路径
    squash = r"D:\内科（压缩）".replace("\\", "/")  # 压缩后存放路径
    tar = r'D:\内科（出书）'.replace("\\", "/")  # 移动到此目录保存图片
    num = 1
    dir = "内01闭光美"
    num = main(f"{squash}/{dir}", num, tar)