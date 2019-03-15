# 10_1 恺撒密码 B
def encode(code):
    LS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ls = "abcdefghijklmnopqrstuvwxyz"
    new_code = ""
    for item in code:
        if item in LS:
            new_code += LS[(LS.index(item)+3)%26]
        elif item in ls:
            new_code += ls[(ls.index(item)+3)%26]
        else:
            new_code += item
    return new_code
code = input()
print(encode(code))
