def main():
    headers = string.split("\n")
    for header in headers:
        key = header.split(": ")[0]
        val = header.split(": ")[1]
        print(f"\t\t'{key}': '{val}',")


if __name__ == "__main__":
    string = """"""
    main()
    