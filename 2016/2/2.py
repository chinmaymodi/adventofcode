import time
start = time.time()
smallfilename = "2/input.txt"
#smallfilename = "2/smalltest.txt"

codelines = []

with open(smallfilename, 'r') as inputfile:
    for line in inputfile:
        codelines.append(line.strip())

kb = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
bigkb = [
    [' ', ' ', '1', ' ', ' '],
    [' ', '2', '3', '4', ' '],
    ['5', '6', '7', '8', '9'],
    [' ', 'A', 'B', 'C', ' '],
    [' ', ' ', 'D', ' ', ' ']
]
x = y = 1
ans = ''
bigx = 2
bigy = 0
bigans = ''

for line in codelines:
    for letter in line:
        match letter:
            case 'U':
                x = max(0, x-1)
                if bigx > 0 and bigkb[bigx-1][bigy] != ' ':
                    bigx -= 1
            case 'D':
                x = min(2, x+1)
                if bigx < 4 and bigkb[bigx+1][bigy] != ' ':
                    bigx += 1
            case 'L':
                y = max(0, y-1)
                if bigy > 0 and bigkb[bigx][bigy-1] != ' ':
                    bigy -= 1
            case 'R':
                y = min(2, y+1)
                if bigy < 4 and bigkb[bigx][bigy+1] != ' ':
                    bigy += 1
    ans += str(kb[x][y])
    bigans += bigkb[bigx][bigy]
print('Answer:')
print(ans)
print('Big Answer:')
print(bigans)
print('Total duration is', time.time() - start)