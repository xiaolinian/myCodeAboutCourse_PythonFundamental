from operator import itemgetter
queue = eval(input())
queue.sort(key = itemgetter(1))
queue.sort(key = itemgetter(0), reverse = True)
output = []
for item in queue:
    output.insert(item[1], item)

print(output)
