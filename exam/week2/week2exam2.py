#week2 exam2
energyvalue = input()
if energyvalue[-1] == "J":
    newenergyvalue = eval(energyvalue[0:-1])/4.185852283
    print("{:.3f}cal".format(newenergyvalue))
else:
    newenergyvalue = eval(energyvalue[0:-3])*4.185852283
    print("{:.3f}J".format(newenergyvalue))


# 29.385  29.384
# 29.494  29.493

# 4.185809
# 4.185827
# 4.185853
# 4.185852
