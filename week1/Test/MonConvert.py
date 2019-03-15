MonStr = input();
if MonStr[0:3] in ["RMB",'rmb']:
  D = eval(MonStr[3:])*6.78
  print("USD{:.2f}".format(D))
else:
  R = eval(MonStr[3:])/6.78
  print("RMB{:.2f}".format(R))
