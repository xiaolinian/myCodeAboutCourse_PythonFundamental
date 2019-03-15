##def displayRange(lower,upper):
##    '''Outputs the numbers from lower to upper.'''
##    while lower <= upper:
##        print(lower)
##        lower = lower + 1
##
##
##displayRange(1,10)

##def displayRange(lower,upper):
##    if(lower<=upper):
##        print(lower)
##        displayRange(lower+1,upper)
##displayRange(1,900)

def ourSum(lower,upper,margin = 0):
    '''Returns the sum of the numbers from lower to upper,
    and outputs a trace of the arguments and return values
    on each call.'''
    blanks = " " * margin
    print(blanks,lower,upper)
    if lower > upper:
        print(blanks,0)
        return 0
    else:
        result = lower + ourSum(lower+1,upper,margin+4)
        print(blanks,result)
        return result
ourSum(1,4)
