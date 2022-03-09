import time


def main():
    print("-----执行开始-----")
    for i in range(101):
        print("\r{:3}%".format(i), end="")
        time.sleep(0.1)
    print("\n-----执行结束-----")


if __name__ == "__main__":
    main()
