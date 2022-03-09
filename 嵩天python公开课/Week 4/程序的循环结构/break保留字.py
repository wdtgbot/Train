for c in "PYTHON":
    if c == "T":
        break
    print(c, end="")
    
s = "PYTHON"
while s != "":
    for c in s:
        print(c, end="")
    s = s[:-1]

s = "PYTHON"
while s != "":
    for c in s:
        if c == "T":
            break  # 只能跳出当前最内层循环
        print(c, end="")
    s = s[:-1]
