# f2 3位水仙花数计算B
def flowercal():
    flowerls = []
    for i in range(100,1000):
        if i == (i//100)**3 + ((i%100)//10)**3 + (i%10)**3:
            flowerls.append(i)
    print(",".join(str(item) for item in flowerls))
flowercal()
