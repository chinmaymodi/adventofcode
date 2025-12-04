from calendar import c
import time
timestart = time.time()
file = "4/smallinput.txt"
file = "4/biginput.txt"

ans1 = 0
ans2 = 0
with open(file, 'r') as inputfile:
    grid = [line.strip() for line in inputfile.readlines()]
    rows = len(grid)
    cols = len(grid[0])
    part2check = set()
    neighbors = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        line = grid[i]
        for j in range(cols):
            if line[j] == '@':
                for x in (-1, 0, 1):
                    for y in (-1, 0, 1):
                        if 0 <= i+x < rows and 0 <= j+y < cols and grid[i+x][j+y] == '@':
                            neighbors[i+x][j+y] += 1
    # for n in neighbors:
    #     print(n)
    for i in range(rows):
        for j in range(cols):
            if neighbors[i][j] <= 4 and grid[i][j] == '@':
                part2check.add((i, j))
                ans1 += 1
    seen = set()
    while part2check:
        i, j = part2check.pop()
        if (i, j) in seen:
            continue
        ans2 += 1
        seen.add((i, j))
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == y == 0:
                    continue
                ni, nj = i+x, j+y
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == '@':
                    neighbors[ni][nj] -= 1
                    if (ni, nj) not in seen and (ni, nj) not in seen:
                        if neighbors[ni][nj] <= 4:
                            part2check.add((ni, nj))
        
    

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)