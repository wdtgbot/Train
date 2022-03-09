from os import listdir, mkdir
from shutil import move
from time import sleep

from keyboard import wait
from pyautogui import mouseDown, mouseUp, hotkey, press, typewrite, click


def mouse(_x, _y, _s=0.75, _t=1):
    """
    鼠标点击
    :param _x: x轴坐标
    :param _y: y轴坐标
    :param _s: 点击后的等待时间
    :param _t: 点击次数
    :return:
    """
    click(_x, _y, clicks=_t, button='left', duration=0.01)
    sleep(_s)


def finger(_str, _s=0.75):
    """
    敲击键盘
    :param _str: 敲击的键位
    :param _s: 点击后的等待时间
    :return:
    """
    press(_str)
    sleep(_s)


def drag(_x, _y, _m, _n):
    """
    鼠标拖动
    :param _x: 原x轴坐标
    :param _y: 原y轴坐标
    :param _m: 拖动到x轴坐标
    :param _n: 拖动到y轴坐标
    :return:
    """
    mouseDown(_x, _y, button='left')
    mouseUp(_m, _n, duration=0.01, button='left')


def enter(_str, _s=0.75, _t=0.01):
    """
    输入字符
    :param _str: 需要输入的字符串
    :param _s: 休眠时间
    :param _t: 拖动持续时间
    :return:
    """
    typewrite(message=str(_str), interval=_t)
    sleep(_s)


def hot(_key1, _key2, *_key3, _s=0.75):
    """
    设置快捷键
    :param _key1: 快捷键1
    :param _key2: 快捷键2
    :param _key3: 快捷键3（并不是必须）
    :param _s: 程序执行完毕后的等待时间
    :return:
    """
    if _key3:
        hotkey(_key1, _key2, _key3[0])
    else:
        hotkey(_key1, _key2)
    sleep(_s)


def _1():
    finger("v")  # 按下v键，使用移动工具
    mouse(806, 510, _s=0.01)  # 点击屏幕正中
    hot("ctrl", "c", _s=0.75)  # 复制图层
    hot("ctrl", "w", _s=1)  # 关闭当前JPG
    finger("n")  # 警告窗口，选择不保存图片


def _2():
    hot("ctrl", "v", _s=0.5)  # 直接回到PSD图，粘贴
    hot("ctrl", "t", _s=0)  # 自动按下调整，手动调整一下


def _3(_m, _tar):
    """
    第二步，主要是保存操作，最后需要判断是否还需要处理下一张图片
    :param _m: 保存的文件名
    :param _tar: 正在进行处理的文件名
    :return:
    """
    finger("enter", _s=0.75)
    hot("ctrl", "shift", "s", _s=1)  # 完成调整，按下另存为快捷键
    enter(str(_m), _s=0.15)  # 输入文件名
    mouse(181, 771, _s=0)  # 点击空白区域
    mouse(344, 834, _s=0.1)  # 点击格式
    mouse(221, 608, _s=0)  # 选择JPEG
    finger("enter", _s=1)  # 回车以确定设置
    finger("enter", _s=1.25)  # 回车以确定设置
    # mouse(1072, 253)  # 点击确定保存按钮
    hot("ctrl", "d", _s=0.25)  # 取消选区
    finger("delete", _s=0.25)  # 删除图层
    if _m != 1:  # 如果还需要继续处理图片
        mouse(310, 75, _s=0.2)  # 点击第二张打开的图片
        finger("m", _s=0.5)  # 按下m键，使用截取工具
        drag(577, 211, 1066, 894)  # 默认截取区域
    else:
        _dir = r"C:\Users\10169\Desktop\pic".replace("\\", "/")
        _new_dir = f"D:\\内科\\原图\\{_tar}"
        mkdir(_new_dir)
        for name in listdir(_dir):
            if name.endswith(".psd"):
                continue
            path = f"{_dir}/{name}"
            move(path, _new_dir)


if __name__ == "__main__":
    while int(input()):
        target = input("请输入pdf文件名：")
        pic = int(input("请输入需要处理的图片张数："))
        hot("alt", "tab")
        wait("`")
        # finger("shift", _s=1)
        mouse(1581, 70, _s=0.25)
        mouse(1609, 77, _s=0.25)
        mouse(310, 75, _s=0)  # 点击第二张打开的图片
        finger("m", _s=0.4)  # 按下m键，使用截取工具
        drag(577, 211, 1066, 894)  # 默认截取区域
        while pic:
            print(f"\r准备处理第{pic}页图片！", end="")
            wait("`")
            _1()
            print("\r准备粘贴图片~", end="")
            wait("`")
            _2()
            print(f"\r保存第{pic}页图片！", end="")
            wait("`")
            _3(pic, target)
            pic -= 1
        print(f"\r完成处理{target}文件！", end="")
