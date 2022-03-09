import random


def main():
    offices = [[], [], []]
    names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    for name in names:
        index = random.randint(0, 2)  # 0,1,2
        offices[index].append(name)
    
    i = 1
    for office in offices:
        print("第%d个办公室的人数为%d" % (i, len(office)))
        i = i + 1
        for name in office:
            print("%s" % name, end="\t")
        print("\n")


if __name__ == '__main__':
    main()
    