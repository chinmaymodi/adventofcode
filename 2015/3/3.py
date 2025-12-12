import time
timestart = time.time()
file = "3/smallinput.txt"
file = "3/biginput.txt"

ans1 = 0
ans2 = 0

with open(file, 'r') as inputfile:
    visited = set()
    x, y = 0, 0
    visited.add((x, y))
    p2santavisited = visited.copy()
    ptrobosantavisited = visited.copy()
    sx, sy = 0, 0
    rx, ry = 0, 0
    d = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
    filelines = inputfile.readlines()
    alt = True
    for line in filelines:
        a = line.strip()
        for ch in a:
            dx, dy = d[ch]
            x += dx
            y += dy
            visited.add((x, y))
            if alt:
                sx += dx
                sy += dy
                p2santavisited.add((sx, sy))
            else:
                rx += dx
                ry += dy
                ptrobosantavisited.add((rx, ry))
            alt = not alt
        ans1 = len(visited)
        ans2 = len(p2santavisited|ptrobosantavisited)

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)