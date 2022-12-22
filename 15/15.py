import time
start_time = time.time()
data = None
with open('milan.txt') as f:
    data = set([tuple([int(y.replace(',', '').replace(':', '')[2:]) for y in x.split() if '=' in y]) for x in f.readlines()])

beacon_searching_y = 2000000

no_beac_y_coords = set()

for pair in data:
    beacon_sensor_dist = abs(pair[0] - pair[2]) + abs(pair[1] - pair[3])
    vertical_sensor_y_dist = abs(pair[1] - beacon_searching_y)
    remaining_x = beacon_sensor_dist - vertical_sensor_y_dist
    for i in range(pair[0] - remaining_x, pair[0] + remaining_x):
        no_beac_y_coords.add(i)
print(len(no_beac_y_coords), end=' ')
end_time = time.time()
print(f"{(end_time - start_time)*1000:.2f} ms")

start_time = time.time()

positive_diagonals = []
negative_diagonals = []

for pair in data:
    manh_dist = abs(pair[0] - pair[2]) + abs(pair[1] - pair[3])
    positive_diagonals.append(pair[1] + manh_dist - pair[0])
    positive_diagonals.append(pair[1] - manh_dist - pair[0])
    negative_diagonals.append(abs(pair[1] + manh_dist + pair[0]))
    negative_diagonals.append(abs(pair[1] - manh_dist + pair[0]))

pos_diag = None
neg_diag = None

found = False
for i in range(len(positive_diagonals)):
    if not found:
        for j in range(i, len(positive_diagonals)):
            if abs(positive_diagonals[i] - positive_diagonals[j]) == 2:     
                pos_diag = min(
                    positive_diagonals[i], positive_diagonals[j]) + 1
                found = True
                break

found = False
for i in range(len(negative_diagonals)):
    if not found:
        for j in range(i, len(negative_diagonals)):
            if abs(negative_diagonals[i] - negative_diagonals[j]) == 2:
                neg_diag = min(negative_diagonals[i], negative_diagonals[j]) + 1
                found = True
                break
                
x = (neg_diag - pos_diag)//2
y = x + pos_diag
print(x * 4000000 + y, end=' ')
end_time = time.time()
print(f"{(end_time - start_time)*1000:.2f} ms")