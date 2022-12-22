import time

start = time.time()
data = []
with open('C:/Users/Luka/Documents/aoc/14/input.txt') as f: # with open('C:/Users/Luka/Documents/aoc/14/input.txt') as f:
    for line in f.readlines():
        data.append([[int(y) for y in x.split(',')]
                    for x in line.strip().split(' -> ')])

sand_start = [500, 0]

wall = []
for row in data:
    for index_of_pair in range(len(row) - 1):
        if row[index_of_pair][0] < row[index_of_pair + 1][0]:
            for j in range(row[index_of_pair][0], row[index_of_pair + 1][0] + 1):
                if [j, row[index_of_pair][1]]not in wall:
                    wall.append(tuple([j, row[index_of_pair][1]]))
        elif row[index_of_pair][0] > row[index_of_pair + 1][0]:
            for j in range(row[index_of_pair + 1][0], row[index_of_pair][0] + 1):
                if [j, row[index_of_pair][1]] not in wall:
                    wall.append(tuple([j, row[index_of_pair][1]]))
        elif row[index_of_pair][1] < row[index_of_pair + 1][1]:
            for j in range(row[index_of_pair][1], row[index_of_pair + 1][1] + 1):
                coord = [row[index_of_pair][0], j]
                if [row[index_of_pair][0], j] not in wall:
                    wall.append(tuple([row[index_of_pair][0], j]))
        elif row[index_of_pair][1] > row[index_of_pair + 1][1]:
            for j in range(row[index_of_pair + 1][1], row[index_of_pair][1] + 1):
                if [row[index_of_pair][0], j] not in wall:
                    wall.append(tuple([row[index_of_pair][0], j]))
wall = set(wall)
stuck_sand = set()
len_stuck_sand = 1
max_y = max([y[1] for y in wall])
while True:
    if len(stuck_sand) == len_stuck_sand:
        break
    len_stuck_sand = len(stuck_sand)
    curr_sand_bit = [sand_start[0], sand_start[1]]
    moved_last_iter = True
    while moved_last_iter:
        moved_last_iter = False
        if tuple([curr_sand_bit[0], curr_sand_bit[1] + 1]) not in wall and tuple([curr_sand_bit[0], curr_sand_bit[1] + 1]) not in stuck_sand:
            curr_sand_bit[1] += 1
            moved_last_iter = True
        #elif check one down and one left
        elif tuple([curr_sand_bit[0] - 1, curr_sand_bit[1] + 1]) not in wall and tuple([curr_sand_bit[0] - 1, curr_sand_bit[1] + 1]) not in stuck_sand:
            curr_sand_bit[0] -= 1
            curr_sand_bit[1] += 1
            moved_last_iter = True
        #elif check one down and one right
        elif tuple([curr_sand_bit[0] + 1, curr_sand_bit[1] + 1]) not in wall and tuple([curr_sand_bit[0] + 1, curr_sand_bit[1] + 1]) not in stuck_sand:
            curr_sand_bit[0] += 1
            curr_sand_bit[1] += 1
            moved_last_iter = True
        else:
            moved_last_iter = False
            stuck_sand.add(tuple(curr_sand_bit))
        if curr_sand_bit[1] == max_y:
            print(len(stuck_sand), end = ' ')
            break
end_time = time.time()
print(f"{(end_time - start)*1000:.2f} ms")
            
# ------------------------------- part2 -------------------------------
start = time.time()
floorY = max_y + 2
stuck_sand = set()
len_stuck_sand = 1
while True:
    if len(stuck_sand) == len_stuck_sand:
        break
    len_stuck_sand = len(stuck_sand)
    curr_sand_bit = [sand_start[0], sand_start[1]]
    moved_last_iter = True
    while moved_last_iter:
        moved_last_iter = False
        if tuple([curr_sand_bit[0], curr_sand_bit[1] + 1]) not in wall and tuple([curr_sand_bit[0], curr_sand_bit[1] + 1]) not in stuck_sand and curr_sand_bit[1] + 1 < floorY:
            curr_sand_bit[1] += 1
            moved_last_iter = True
        #elif check one down and one left
        elif tuple([curr_sand_bit[0] - 1, curr_sand_bit[1] + 1]) not in wall and tuple([curr_sand_bit[0] - 1, curr_sand_bit[1] + 1]) not in stuck_sand and curr_sand_bit[1] + 1 < floorY:
            curr_sand_bit[0] -= 1
            curr_sand_bit[1] += 1
            moved_last_iter = True
        #elif check one down and one right
        elif tuple([curr_sand_bit[0] + 1, curr_sand_bit[1] + 1]) not in wall and tuple([curr_sand_bit[0] + 1, curr_sand_bit[1] + 1]) not in stuck_sand and curr_sand_bit[1] + 1 < floorY:
            curr_sand_bit[0] += 1
            curr_sand_bit[1] += 1
            moved_last_iter = True
        else:
            moved_last_iter = False
            stuck_sand.add(tuple(curr_sand_bit))
            if curr_sand_bit == [500, 0]:
                print(len(stuck_sand), end = ' ')
                end_time = time.time()
                print(f"{(end_time - start)*1000:.2f} ms")
                exit(0)