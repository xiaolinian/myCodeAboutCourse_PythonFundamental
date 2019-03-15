#1 快乐的数字
def happynum(num):
    new_num = 0
    for i in range(1,100):
        if num == 1:
            return True
            break
        else:
            for item in str(num):
                new_num += eval(item)**2
                num = new_num
    else:
        return False
num = input()
print(happynum(num))

