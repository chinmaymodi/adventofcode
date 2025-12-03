import time
start = time.time()
smallfilename = "1/input.txt"

x = y = 0
f = (0, 1)
rnext = {
    (0, 1):(1, 0),
    (1, 0):(0, -1),
    (0, -1):(-1, 0),
    (-1, 0):(0, 1)
}
lnext = {rnext[i]:i for i in rnext}

directions = []
seen = set()
seen.add((0, 0))
firstdupe = False

with open(smallfilename, 'r') as inputfile:
    line = inputfile.readline()    
    directions = line.strip().split(', ')

for d in directions:
    turn = d[0]
    steps = int(d[1:])
    if turn == 'R':
        f = rnext[f]
    else:
        f = lnext[f]
    if not firstdupe:
        while steps:
            x += 1 * f[0]
            y += 1 * f[1]
            if (x, y) in seen:
                print('First doubler is', x, y)
                print('Its distance is:')
                print(abs(x)+abs(y))
                firstdupe = True
            seen.add((x, y))
            steps -= 1
    else:
        x += steps * f[0]
        y += steps * f[1]

print('Final distance is:')
print(abs(x) + abs(y))
print('Total duration is', time.time() - start)