import json, copy
data = [[]]
with open('input.txt') as f:  # C:/Users/Luka/Documents/aoc/d13/
    for line in [x.strip() for x in f]:
        if line == '':
            data.append([])
            continue
        data[-1].append(json.loads(line))
data0 = copy.deepcopy(data)

def is_correctly_sorted(list1, list2):
    i = 0
    while i < min(len(list1), len(list2)):
        if type(list1[i]) == int and type(list2[i]) == int:
            if list1[i] < list2[i]:
                return 1
            elif list1[i] > list2[i]:
                return -1
        elif type(list1[i]) == list and type(list2[i]) == list:
            if len(list2[i]) == 0 and len(list1[i]) != 0:
                return -1

            if len(list1[i]) == 0 and len(list2[i]) != 0:
                return 1

            if is_correctly_sorted(list1[i], list2[i]) == 1:
                return 1

            if is_correctly_sorted(list1[i], list2[i]) == -1:
                return -1

        elif type(list1[i]) != type(list2[i]):
            if type(list1[i]) == int:
                list1[i] = [list1[i]]
            else:
                list2[i] = [list2[i]]
            i -= 1
        i += 1
    if len(list1) < len(list2):
        return 1
    elif len(list1) > len(list2):
        return -1
    else:
        return 0
c = 0
for i in range(1, len(data) + 1):
    if is_correctly_sorted(*data[i - 1]) == 1:
        c += i
print(c)

# -- clumsy
data, data2 = data0, []
for elem in data:
    data2.append(elem[0])
    data2.append(elem[1])
data = data2
data.append([[2]])
data.append([[6]])

changes = True
while changes:
    changes = False
    for i in range(len(data) - 1):
        if is_correctly_sorted(data[i], data[i + 1]) == -1:
            data[i], data[i + 1] = data[i + 1], data[i]
            changes = True

prod = 1
for i in range(len(data)):
    line = str(data[i])
    if ',' in line: continue
    if '[2]' in line:
        prod *= i + 1
    elif '[6]' in line:
        prod *= i + 1
print(prod)