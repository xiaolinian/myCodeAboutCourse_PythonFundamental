# test5:长度转换
a = input()
if a[-1] in ['m']:
    inch = eval(a[0:-1])/39.37
    print("{:.2f}in".format(inch))
else:
    meter = eval(a[0:-2]) * 39.37
    print("{:.2f}m".format(meter))
    
