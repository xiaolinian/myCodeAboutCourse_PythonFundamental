def facobboni(n):
    if n==1 or n==2:
        return 1
    else:
        return facobboni(n-1)+facobboni(n-2)
for i in range(1,11,2):
    print(facobboni(i))
