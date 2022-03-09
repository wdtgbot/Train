# 示例一
try:
    num = eval(input("请输入一个整数："))
    print(num ** 2)
except:
    print("输入的不是整数！")
    
# 示例二
try:
    num = eval(input("请输入一个整数："))
    print(num ** 2)
except NameError:
    print("输入的不是整数！")
    
# 高级用法
"""
try:
    <语句1>
except:
    <语句2>
else:
    <语句3> 不发生异常时运行
finally:
    <语句4> 不管是否发生异常都运行
"""
