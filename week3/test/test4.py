# 星号三角形I
n = input()
N = eval(n)
for i in  range(N//2+1):
    print("{:^50}".format((i*2+1)*'*'))
