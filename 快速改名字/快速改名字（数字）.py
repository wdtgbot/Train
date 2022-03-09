from shutil import copy
from os import listdir, rename


def main(path, num, target_dir):
    files = listdir(path)
    files.sort(key=lambda x: int(x.split(".")[0]))
    for file in files:
        new_file_name = str(num + 1)
        old_file_path = f"{path}/{file}"
        new_file_path = f"{path}/{new_file_name}.jpg"
        rename(old_file_path, new_file_path)
        copy(new_file_path, target_dir)
        print(old_file_path, new_file_path)
        num += 1


if __name__ == "__main__":
    dir = r'D:\妇产科\妇产科出书——压缩'
    main(r"D:\妇产科\20211125已经处理的妇产科判决书\妇产72史志源二审判决书——压缩", 717, dir)
    main(r'D:\妇产科\20211125已经处理的妇产科判决书\妇产77张琼艳、陆继永一审判决书——压缩', 729, dir)
    main(r'D:\妇产科\20211125已经处理的妇产科判决书\妇产75孙显兰案一审判决书——压缩', 740, dir)
    main(r'D:\妇产科\20211125已经处理的妇产科判决书\妇产74刘琼一审判决书——压缩', 750, dir)
    main(r'D:\妇产科\20211125已经处理的妇产科判决书\妇产73刘琼之女一审判决书——压缩', 765, dir)
    main(r'D:\妇产科\20211125已经处理的妇产科判决书\妇产76王海燕、赵俊永案一审判决书——压缩', 776, dir)
    main(r'D:\妇产科\20211125已经处理的妇产科判决书\妇产78李顺良二审判决书——压缩', 787, dir)
