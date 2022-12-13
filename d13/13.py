import json

data = [[]]
with open('C:/Users/Luka/Documents/aoc/d13/example.txt') as f:
    for line in [x.strip() for x in f]:
        if line == '':
            data.append([])
            continue
        data[-1].append(json.loads(line))


def list_cmp(list1, list2): # ret 1 -> success, ret 0 -> they're equal, ret -1 -> fail, should propagate immediately to the end and return false
    equal = True
    for i in range(min(len(list1), len(list2))):
        # if they're both of type int
        if type(list1[i]) == int and type(list2[i]) == int:
            if list1[i] > list2[i]:
                return -1
            elif list1[i] != list2[i]:
                equal = False
        # if they're both of type list
        elif type(list1[i]) == list and type(list2[i]) == list:
            ret = list_cmp(list1[i], list2[i])
            if ret == -1:
                return -1
            elif ret == 0:
                return -1 if len(list1[i]) > len(list2[i]) else 0
        else: # different types, int and list or list and int
            




correctly_sorted = []
c = 0
for i in range(1, len(data) + 1):
    print("---------------------------------------------------")
    if list_cmp(*data[i - 1]):
        c += i
        correctly_sorted.append(i)
        print(i)
print('-------------------')
print(c)
print(*correctly_sorted, sep = ' ')
