from random import random
from time import perf_counter


datrs = 1000 * 1000
hits = 0.0
start = perf_counter()
for i in range(1, datrs + 1):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits += 1
p = 4 * (hits/datrs)
print("圆周率值是：{}".format(p))
print("运行时间是：{:.5f}".format(perf_counter() - start))
