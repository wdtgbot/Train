guess = eval(input("猜一下数字："))
if guess == 99:
    print("猜对了")
else:
    print("猜错了")
    
# 紧凑方式
guess = eval(input("猜一下数字："))
print("猜对了") if guess == 99 else print("猜错了")
print("猜{}了".format("对" if guess == 99 else "错"))
