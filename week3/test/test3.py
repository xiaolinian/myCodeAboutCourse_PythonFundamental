# 天天向上的力量III
n = input()
N = eval(n)
workhard = (1.0+N/1000)**365
notworkhard = (1.0-N/1000)**365
div = workhard // notworkhard
print("{:.2f},{:.2f},{:.0f}".format(workhard,notworkhard,div))
