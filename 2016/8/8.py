import time
start = time.time()

filename = "8/input.txt"
# filename = "8/smalltest.txt"

ans = 0
ans2 = ''

def pp(rect: list[list]):
    for row in rect:
        ctr = 0
        for letter in row:
            print(letter, end = '')
            ctr += 1
            if ctr % 5 == 0:
                print('  ', end = '')
        print()

rownum = 6
colnum = 50
rect = [[' ' for _ in range(colnum)] for _ in range(rownum)]
# pp(rect)


with open(filename, 'r') as inputfile:
    for line in inputfile:
        line = line.strip()
        tokens = line.split(' ')
        if tokens[0] == 'rect':
            cols, rows = map(int, tokens[1].split('x'))
            for i in range(rows):
                for j in range(cols):
                    if rect[i][j] != '#':
                        ans += 1
                        rect[i][j] = '#'
        else:
            shiftamount = int(tokens[4])
            index = int(tokens[2].split('=')[1])
            if tokens[1] == 'row':
                shiftamount %= colnum
                rect[index] = rect[index][-shiftamount:] + rect[index][:-shiftamount]
            else:
                shiftamount %= rownum
                oldcolvals = [rect[i][index] for i in range(rownum)]
                newcolvals = oldcolvals[-shiftamount:] + oldcolvals[:-shiftamount]
                for i in range(rownum):
                    rect[i][index] = newcolvals[i]
pp(rect)
        
        
print('Answer:')
print(ans)

print('Answer part 2:')
print(ans2)

print('Total duration is', time.time() - start)