def fib(max):
    max = eval(max)
    sum = 0
    if max == 0:
        lst = [0]
    else:
        lst = [0,1]
    while lst[-1] < max:
        lst.append(lst[-1]+lst[-2])
    for item in lst:
        sum += item
    lst.append(sum)
    m = sum/len(lst)
    for item in lst:
        print("{}, ".format(item),end="")
    print("{:,.0f}".format(m))
n=input()
fib(n)
    
