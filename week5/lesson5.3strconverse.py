def strconverse(str):
    if str== "":
        return str;
    else:
        return strconverse(str[1:])+str[0]

strafterconverse=strconverse("abcdefg")
print(strafterconverse)
