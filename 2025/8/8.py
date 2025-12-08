import time
timestart = time.time()
from UnionFind import UnionFind
from heapq import heappop, heapify
file = "8/smallinput.txt"
file = "8/biginput.txt"

ans1 = 0
ans2 = 0
with open(file, 'r') as inputfile:
    junctionheap = []
    xs, ys, zs = [], [], []
    for line in inputfile:
        x, y, z = map(int, line.strip().split(','))
        xs.append(x); ys.append(y); zs.append(z)

    n = len(xs)
    uf = UnionFind(n)

    for j in range(n):
        x2, y2, z2 = xs[j], ys[j], zs[j]
        for i in range(j):
            dx, dy, dz = xs[i] - x2, ys[i] - y2, zs[i] - z2
            dist = dx*dx + dy*dy + dz*dz
            junctionheap.append((dist, i, j))
    heapify(junctionheap)

    itemstocombine = 10 if file == "8/smallinput.txt" else 1000
    ctr = 0
    components = n
    while len(junctionheap) > 0:
        ctr += 1
        dist, i, j = heappop(junctionheap)
        merged = uf.union(i, j)
        if ctr == itemstocombine:
            roots = set(uf.find(k) for k in range(n))
            sizes = sorted(uf.size[r] for r in roots)
            ans1 = sizes[-1] * sizes[-2] * sizes[-3]
        if merged:
            components -= 1
            if components == 1:
                ans2 = xs[i] * xs[j]
                break
print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)
