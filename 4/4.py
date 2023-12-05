data = [[[int(x) for x in part.split('-')] for part in line.strip().split(',')] for line in open('input.txt', 'r').readlines()]

s = [0, 0]
for line in data:
    if line[0][0] >= line[1][0] and line[0][1] <= line[1][1] or line[1][0] >= line[0][0] and line[1][1] <= line[0][1]:
        s[0] += 1
    
    if line[0][0] <= line[1][0] and line[0][1] >= line[1][0] or line[1][0] <= line[0][0] and line [1][1] >= line[0][0]:
        s[1] += 1

print(f"{s[0]}\n{s[1]}")