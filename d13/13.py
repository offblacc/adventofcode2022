import json

data = [[]]
with open('C:/Users/Luka/Documents/aoc/d13/example.txt') as f:
    for line in [x.strip() for x in f]:
        if line == '':
            data.append([])
            continue
        data[-1].append(json.loads(line))


def is_correctly_sorted(list1, list2):  # compare lists
    print("Comparing lists", list1, "|AND|", list2)
    unresolved_int_comparing = True
    for i in range(min(len(list1), len(list2))):
        if type(list1[i]) == int and type(list2[i]) == int:
            print(f"Comparing {list1[i]} and {list2[i]}, both integers.")
            if list1[i] > list2[i]:
                print("Left side bigger. Returning false.")
                return False
            elif list1[i] < list2[i]:
                print("Right side bigger. Remembering for later so that we know whether we need a tie breaker or not - list size.")
                unresolved_int_comparing = False

        # xor of types, if one is list and the other isn't
        elif type(list1[i]) != type(list2[i]):
            if type(list1[i]) == int:
                if not is_correctly_sorted([list1[i]], list2[i]):
                    return False
            else:
                if not is_correctly_sorted(list1[i], [list2[i]]):
                    return False
        else: # both lists
            if not is_correctly_sorted(list1[i], list2[i]):
                return False

    if unresolved_int_comparing:
        print("Unresolved int comparing. Determining result based on list size.")
        if len(list1) > len(list2):
            print("Left side bigger. Returning false.")
            return False


    return True

correctly_sorted = []
c = 0
for i in range(1, len(data) + 1):
    print("---------------------------------------------------")
    if is_correctly_sorted(*data[i - 1]):
        c += i
        correctly_sorted.append(i)
        print(i)
print('-------------------')
print(c)
print(*correctly_sorted, sep = ' ')
