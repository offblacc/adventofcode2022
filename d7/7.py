class dir:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.dirs = []
        self.size = None
        self.parent = None
    
    def __repr__(self):
        return self.name

    def printRecursively(self, ident=0):
        print(ident * " " + '-' + " " + self.name + ' (dir)')
        for d in self.dirs:
            d.printRecursively(ident+1)
        for f in self.files:
            print(" " * (ident+1) + '-' + " " + f.name + ' (file, size=' + str(f.size) + ')')

class file:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def __repr__(self):
        return self.name

def dir_sizes(dir, total_sizes_conditional=0):
    dir.size = sum([f.size for f in dir.files])
    for d in dir.dirs:
        dir.size += dir_sizes(d)[0]
        total_sizes_conditional += dir_sizes(d)[1]
    if dir.size < 100000:
        total_sizes_conditional += dir.size
    return dir.size, total_sizes_conditional


tree = dir('/')
curr_node = tree
for line in [x.split() for x in open('input.txt')]:
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '/':
                curr_node = tree
            elif line[2] == '..':
                curr_node = curr_node.parent if curr_node.parent else None
            else:
                if line[2] not in [d.name for d in curr_node.dirs]:
                    curr_node.dirs.append(dir(line[2]))
                    curr_node.dirs[-1].parent = curr_node
                for n in curr_node.dirs:
                    if n.name == line[2]:
                        curr_node = n
                        break
        elif line[1] == 'ls':
            continue
    elif line[0] == 'dir':
        curr_node.dirs.append(dir(line[1]))
        curr_node.dirs[-1].parent = curr_node
    else:
        curr_node.files.append(file(line[1], int(line[0])))

print(dir_sizes(tree)[1])

should_free_up = dir_sizes(tree)[0] - 40000000
print(f"should free up {should_free_up} bytes")

def get_sizes(dir):
    sizes = []
    for d in dir.dirs:
        sizes.append(dir_sizes(d)[0])
        sizes += get_sizes(d)
    return sizes
all_dir_sizes = get_sizes(tree)
print(sorted(all_dir_sizes))
for size in sorted(all_dir_sizes):
    if size >= should_free_up:
        print(size)
        break