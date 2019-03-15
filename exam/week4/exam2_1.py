#1 快乐的数字
def happynum(num):
    new_num = 0
    if num == 1:
        return True
    else:
        try:
            for item in str(num):
                new_num += eval(item)**2
                return happynum(new_num)
        except RuntimeError:
            return False   
for i in range(1,1000):
    print("{},{}".format(i,happynum(i)))
