from PIL import Image
from glob import glob
from os import mkdir


def main(dir_name):
    path_file_number = glob(f'{dir_name}\\*.jpg')
    i = 1
    new_dir_name = f"{dir_name}——压缩"
    mkdir(new_dir_name)
    while i <= len(path_file_number):
        print(f"处理着第{i}张图片……")
        img = Image.open(f'{dir_name}\\{i}.jpg')
        img.save(f'{new_dir_name}\\{i}.jpg', quality=25)  # quality 为图片质量 100表示不压缩， 75表示压缩比例
        i = i + 1


if __name__ == "__main__":
    main(r'D:\妇产科\20211125已经处理的妇产科判决书\妇产81李顺良二审判决书')
