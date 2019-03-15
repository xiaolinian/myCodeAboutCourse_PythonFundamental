# 假设每考一次试的费用为X，每次考试通过的概率为P1.求考试通过的成本的数学期望。
def totalcost(X,P1):
    totalcost=0
    for i in range(1,100):
        #print(i)
        costith=X*i*P1*pow(1-P1,i-1)
        #print(costith)
        totalcost+=costith
    print(totalcost)

totalcost(4500,0.95)
totalcost(2500,0.4)

        

