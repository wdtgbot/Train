from PIL import Image
from glob import glob
from os import mkdir


def squash_jpg(_init, _squash, _dir):
    i = 1
    _file_account = glob(f'{_init}/{dir}/*.jpg')
    _new_dir = f"{squash}/{dir}"
    try:
        mkdir(_new_dir)
    except FileExistsError:
        pass
    while i <= len(_file_account):
        print(f"处理着第{i}张图片……")
        img = Image.open(f'{_init}/{_dir}/{i}.jpg')
        img.save(f'{_new_dir}/{i}.jpg', quality=20)  # quality 为图片质量 100表示不压缩， 75表示压缩比例
        i = i + 1


if __name__ == "__main__":
    init = r"D:\内科（原图）"  # 原图路径
    squash = r"D:\内科（压缩）"  # 压缩后存放路径
    dir = "内01闭光美"  # 处理的子目录名称
    squash_jpg(init, squash, dir)
