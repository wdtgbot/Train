import pyautogui
from time import sleep
currentMouseX, currentMouseY = pyautogui.position()
print(f"{currentMouseX}, {currentMouseY}")

i = int(input("需要处理多少张图片？"))
pyautogui.hotkey('alt', 'tab')
m = 0
for _ in range(i):
    pyautogui.press('right')
    pyautogui.press('enter')
    sleep(1.6)
    pyautogui.mouseDown(1657, 473, button='left')
    pyautogui.mouseUp(1657, 894, duration=0.01, button='left')
    pyautogui.press('s')
    pyautogui.mouseDown(1147, 574, button='left')
    pyautogui.mouseUp(1527, 741, duration=0.01, button='left')
    pyautogui.press('delete')
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('alt', 'f4')
    m += 1
    print(f"处理完成第{m}张图片")
    sleep(0.1)


# pyautogui.hotkey('alt', 'tab')
# pyautogui.click(989, 738, clicks=1, button='left', duration=0.1)
# pyautogui.typewrite(message='Hello world!', interval=0.01)
