from keyboard import wait
from pyautogui import position


def main():
    currentMouseX, currentMouseY = position()
    wait("alt")
    print(f"\rmouse({currentMouseX}, {currentMouseY})", end="")


if __name__ == "__main__":
    while True:
        main()
        