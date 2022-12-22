def in_graph(node, heigth, width):
    return node[0] >= 0 and node[0] < heigth and node[1] >= 0 and node[1] < width

def can_step_to(graph, node, new_node):
    return ord(graph[new_node[0]][new_node[1]]) - ord(graph[node[0]][node[1]]) <= 1

def main(part: int):

    data = [x.strip() for x in open('input.txt').readlines()]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_positions = []
    destination = None
    visited = set()

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                current_positions = [(i, j)]
                data[i] = data[i][:j] + 'a' + data[i][j + 1:]
                if current_positions and destination: break
            if data[i][j] == 'E':
                destination = (i, j)
                data[i] = data[i][:j] + 'z' + data[i][j + 1:]
                if current_positions and destination: break
                
    if part == 2:
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] != 'a': continue
                current_positions.append((i, j))
    
    steps = 0
    while destination not in current_positions:
        new_positions = []
        for pos in current_positions:
            for direction in directions:
                new_pos = tuple([sum(x) for x in zip(pos, direction)])
                if in_graph(new_pos, len(data), len(data[0])) and can_step_to(data, pos, new_pos) and new_pos not in new_positions and new_pos not in visited:
                    new_positions.append(new_pos)
                    visited.add(new_pos)

        current_positions = new_positions
        steps += 1
    print(steps)

if __name__ == '__main__':
    main(1)
    main(2)