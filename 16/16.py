data = open('C:/Users/Luka/Documents/aoc/16/input.txt').readlines()

for line in data:
    print(line.split()[1])

data = [x.strip() for x in data if x.strip() != '']

valves = {}
pressures = {}

for line in data:
    pressures.update({line.split()[1]: int(line.split('=')[1].split(';')[0])})
    valve, tunnels = line.split(';')
    valve = valve.split()[1]
    if line.split()[-2] != 'valve':
        tunnels = set(tunnels.split('tunnels lead to valves ')[1].split(', '))
    else:
        tunnels = set([tunnels.split()[-1]])
    valves[valve] = tunnels

# for item in valves.items():
#     for valve in item[1]:
#         print(item[0], valve)

# go from AA, using DFS to build a map of the time it takes to get to each valve

global_max = 0


def dfs(valve='AA', time=30, pressure_relieved=0):
    global global_max
    if time <= 0:
        return
    
    if pressures[valve] != 0:
        for tunnel in valves[valve]:
            new_total = pressure_relieved + pressures[valve]
            if new_total > global_max:
                print(global_max)
                global_max = new_total
            dfs(tunnel, time - 2, new_total)

    
    for tunnel in valves[valve]:
        dfs(tunnel, time - 1, pressure_relieved)
    
dfs()
print(global_max)