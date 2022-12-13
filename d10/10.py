cycle, X, sumofproducts, drawing = 0, 1, 0, ""

for line in [x.strip() for x in open('input.txt').readlines()]:
    for _ in range(1 if line.split()[0] == 'noop' else 2):
        cycle += 1
        if cycle == 20 or (cycle - 20) % 40 == 0:
            sumofproducts += cycle * X
        drawing += "#" if X - 1 <= (cycle - 1) % 40 <= X + 1 else "."
        if cycle % 40 == 0:
            drawing += '\n'
    if line.split()[0] == 'addx':
        X += int(line.split()[1])

print(sumofproducts, drawing, sep='\n')
