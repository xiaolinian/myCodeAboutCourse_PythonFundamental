# 凯撒密码I
str = input()
flag = "abcdefghijklmnopqrstuvwxyzabc"
len = len(str)
result = ''
for i in range(len):
    subStr = str[i]
    if subStr == "":
        result += ""
        continue
    idx=flag.find(subStr)
    result += flag[idx+3]
print(result)
