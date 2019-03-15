def fac(num):
    fac = 1
    for item in range(1,num+1):
        fac *= item
    return fac


def sum_fac(n):
    if n.isdigit():
        sum_fac = 0
        for item in range(1,eval(n)+1):
            sum_fac += fac(item)
        return sum_fac
    else:
        return '输入有误，请输入正整数。'

n = input()
print(sum_fac(n))
