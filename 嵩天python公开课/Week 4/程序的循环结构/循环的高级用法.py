"""
循环与else
- 当循环没有被break语句退出时，执行else语句块
- else语句块作为”正常“完成循环的奖励
- else的用法与异常处理中else用法相似
"""

for c in "PYTHON":
    if c == "T":
        continue
    print(c, end="")
else:
    print("正常退出")
# >>> PYTHON正常退出
    

for c in "PYTHON":
    if c == "T":
        break
    print(c, end="")
else:
    print("正常退出")
# >>> PY
