data = open('input.txt').read().strip()

for st in [4, 14]:
    for i in range(4, len(data)):
        if len(set(data[i - st:i])) == st:
            break
    print(i)