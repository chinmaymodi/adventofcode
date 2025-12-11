import time
timestart = time.time()

from collections import deque, defaultdict
file = "11/smallinput.txt"
file2 = "11/smallinput2.txt"
file = "11/biginput.txt"
file2 = "11/biginput.txt"

ans1 = 0
ans2 = 0
nodes = {}

def topo_sort(nodes) -> list:
    indeg = defaultdict(int)
    for u in nodes:
        for v in nodes[u]:
            indeg[v] += 1
    for u in nodes:
        indeg[u]
    q = deque([u for u in indeg if indeg[u] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in nodes.get(u, []):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order

def count_paths(nodes, start, end, must = ()) -> int:
    must = list(must)
    must_index = {name: i for i,name in enumerate(must)}
    full_mask = (1 << len(must)) - 1

    order = topo_sort(nodes)
    paths = defaultdict(lambda: defaultdict(int))
    paths[start][0] = 1

    for u in order:
        for mask,count in paths[u].items():
            if count == 0: continue
            for v in nodes.get(u, []):
                new_mask = mask
                if v in must_index:
                    new_mask |= (1 << must_index[v])
                paths[v][new_mask] += count

    return paths[end][full_mask]

with open(file, 'r') as inputfile:
    filelines = inputfile.readlines()
    for line in filelines:
        parent, children = line.split(':')
        parent = parent.strip()
        nodes[parent] = children.strip().split(' ')
    ans1 = count_paths(nodes, 'you', 'out')
if file != file2:
    with open(file2, 'r') as inputfile:
        filelines = inputfile.readlines()
        for line in filelines:
            parent, children = line.split(':')
            parent = parent.strip()
            nodes[parent] = children.strip().split(' ')
ans2 = count_paths(nodes, 'svr', 'out', ('fft','dac'))

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)