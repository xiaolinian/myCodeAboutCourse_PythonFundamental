# exam 3 百分制到五级制的转换
def rank_change(score):
    if score.isdigit() and 0<=eval(score)<=100:
        score = eval(score)
        try:
            if 90<=score<=100:
                print('输入成绩属于A级别。')
                print('祝贺你通过考试！')
            elif 80<=score<=89:
                print('输入成绩属于B级别。')
                print('祝贺你通过考试！')
            elif 70<=score<=79:
                print('输入成绩属于C级别。')
                print('祝贺你通过考试！')
            elif 60<=score<=69:
                print('输入成绩属于D级别。')
                print('祝贺你通过考试！')
            elif 50<=score<59:
                print('输入成绩属于E级别。')
            else:
                print('输入成绩属于F级别。')
        except NameError:
            print('输入数据有误！')
        else:
            pass
        finally:
            print('好好学习，天天向上！')
    else:
        print('输入数据有误！')
        print('好好学习，天天向上！')
        

score = input()
rank_change(score)
