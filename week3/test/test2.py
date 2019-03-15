n = input()
N = eval(n)
if N<0:
    N1 = -(abs(N)+10)
    N2 = -(abs(N)-10)
    N3 = -(abs(N)*10)
else:
    N1 = abs(N)+10
    N2 = abs(N)-10
    N3 = abs(N)*10
print("{} {} {} {}".format(N,N1,N2,N3))
