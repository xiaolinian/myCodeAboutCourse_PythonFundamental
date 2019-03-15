def login():
    for i in range(0,3):
        username = input()
        password = input()
        if username == 'Kate' and password == '666666':
            print('登录成功！')
            break
        if i < 2:
            print('输入用户名或程序错误，请重新输入')
        if i == 2:
            print('3次用户名或者密码均有误！退出程序。')
            break
        
login()
