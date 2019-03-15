# 凯撒密码I V2
str = input()
outstr = ""
base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
for c in str:
    if c !="":
        outstr += base[(ord(c) - ord('a') + 3)%26]
    else:
        outstr += ""
print(outstr)
