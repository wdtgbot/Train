p = 0
n = 100
for k in range(n):
    p += 1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
    print("\r圆周率值是：{}".format(p), end="")
    