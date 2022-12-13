data = [x.strip() for x in open('input.txt').readlines()]
visible = 0
for i in range(1, len(data)-1):
    for j in range(1, len(data) - 1):
        isVisible = False
        neighbours = set()
        if not isVisible:
            for k in range(j-1, -1, -1):
                neighbours.add(data[i][k])
            if max(neighbours) < data[i][j]:
                isVisible = True
                visible += 1
            else:
                neighbours = set()        
        
        if not isVisible:
            for k in range(i-1, -1, -1):
                neighbours.add(data[k][j])
            if max(neighbours) < data[i][j]:
                isVisible = True
                visible += 1
            else:
                neighbours = set()
        
        if not isVisible:
            for k in range(j+1, len(data)):
                neighbours.add(data[i][k])
            if max(neighbours) < data[i][j]:
                isVisible = True
                visible += 1
            else:
                neighbours = set()
        
        if not isVisible:
            for k in range(i+1, len(data)):
                neighbours.add(data[k][j])
            if max(neighbours) < data[i][j]:
                isVisible = True
                visible += 1

visible += 4 * (len(data[0])) - 4
print(visible)
mul, max_mul = 1, 1
for i in range(1, len(data) - 1):
    for j in range(1, len(data) - 1):
        #top
        c = 0
        for k in range(i - 1, -1, -1):
            if data[k][j] < data[i][j]:
                c += 1
            else:
                c += 1
                break
        mul *= c
        # right 
        c = 0
        for k in range(j + 1, len(data)):
            if data[i][k] < data[i][j]:
                c += 1
            else:
                c += 1
                break
        mul *= c
        # bottom
        c = 0
        for k in range(i + 1, len(data)):
            if data[k][j] < data[i][j]:
                c += 1
            else:
                c += 1
                break
        mul *= c
        # left
        c = 0
        for k in range(j - 1, -1, -1):
            if data[i][k] < data[i][j]:
                c += 1
            else:
                c += 1
                break
        mul *= c
        max_mul = max(max_mul, mul)
        mul = 1
print(max_mul)