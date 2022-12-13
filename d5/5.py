data = open('input.txt', 'r').read().split('\n')
stacks = [[] for _ in range((len(data[0]) + 1) // 4)]

i = 0
while data[i + 1].strip() != '':
    for j in range(len(stacks)):
        el = data[i][j * 4 + 1]
        if el.strip() != '':
            stacks[j].append(el)
    i += 1
i += 2
starting = i
for stack in stacks: stack.reverse()
stacks_mover_9001 = [stack[:] for stack in stacks]

while i < len(data):
    line = data[i].split()
    for _ in range(int(line[1])):
        stacks[int(line[5]) - 1].append(stacks[int(line[3]) - 1].pop())
    i += 1

for st in stacks:
    print(st[-1], end='')
print()

i = starting

while i < len(data):
    line = data[i].split()
    popping_index = len(stacks_mover_9001[int(line[3]) - 1]) - int(line[1])
    for _ in range(int(line[1])):
        stacks_mover_9001[int(line[5]) - 1].append(stacks_mover_9001[int(line[3]) - 1].pop(popping_index))
    i += 1

for st in stacks_mover_9001:
    print(st[-1], end='')
print()