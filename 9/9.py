def new_pos(tail, head):
    if abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1:
        return tail
    for i in range(2):
        if tail[i] == head[i]:
            if abs(tail[i - 1] - head[i - 1]) > 1:
                return (tail[0], tail[1] + (1 if head[1] > tail[1] else -1)) if i == 0 else (tail[0] + (1 if head[0] > tail[0] else -1), tail[1])
    return (tail[0] + (1 if head[0] > tail[0] else -1), tail[1] + (1 if head[1] > tail[1] else -1))

coords = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

snake_coordinates = [(0, 0) for _ in range(10)]
visited = [set(), set()]
for line in [x.split() for x in open('input.txt').readlines()]:
    for i in range(int(line[1])):
        snake_coordinates[0] = tuple([sum(x) for x in zip(snake_coordinates[0], coords[line[0]])])

        for i in range(1, 10):
            snake_coordinates[i] = new_pos(snake_coordinates[i], snake_coordinates[i - 1])

        visited[0].add(snake_coordinates[1])
        visited[1].add(snake_coordinates[-1])

print(len(visited[0]), len(visited[1]))