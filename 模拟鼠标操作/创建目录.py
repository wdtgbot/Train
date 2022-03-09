from os import listdir, mkdir


def main(_source, _target):
    old_dirs = listdir(_source)
    for old_dir in old_dirs:
        name = old_dir.split(".")[0]
        new = f"{_target}/{name}"
        print(new)
        mkdir(new)
        
        
if __name__ == "__main__":
    main(r"D:\外科", r"D:\外科（原图）")
    