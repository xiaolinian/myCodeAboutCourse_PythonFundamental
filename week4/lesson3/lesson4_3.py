# lesson 4.3
s = "PYTHON"
while s != "":
    for c in s:
        print(c,end="")
    s = s[0:-1]
    print(",",end="")
    
