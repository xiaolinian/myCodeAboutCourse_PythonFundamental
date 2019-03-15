f = open("hamlet.txt", "r", encoding='utf-8').read()
f = f.lower()
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
    f = f.replace(ch, " ")
text = f.split()

count = {}
for word in text:
    count[word] = count.get(word, 0) + 1
top = sorted(count.items(), key = lambda x:x[1], reverse = True)    
for i in range(0, 10):
    print('{:<10},{:>5}'.format(top[i][0], top[i][1]))
