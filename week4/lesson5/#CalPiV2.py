# CalPiV2.py
from random import random
from time import perf_counter
DARTS = 1000*10000
hits = 0
start = perf_counter()
for i in range(1,DARTS+1):
    x,y = random(),random()
    dist = pow(x ** 2 + y ** 2,0.5)
    if dist <= 1.0:
        hits += 1
pi = hits/DARTS * 4
print("圆周率值是:{}".format(pi))
end = perf_counter()
print("运行时间：{}".format(end-start))
