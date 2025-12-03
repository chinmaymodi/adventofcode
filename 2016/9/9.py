import time
start = time.time()

filename = "9/input.txt"
# filename = "9/smalltest.txt"

ans = ''
ans2 = 0

with open(filename, 'r') as inputfile:
    for line in inputfile:
        ans = 0
        line = line.strip()
        # print(line)
        size = 0
        mult = 0
        updatingmult = False
        multtoken = ''
        i = 0
        while i < len(line):
            letter = line[i]
            # print(i)
            # input()
            if updatingmult:
                if letter != ')':
                    multtoken += letter
                    i += 1
                else:
                    updatingmult = False
                    size, mult = map(int, multtoken.split('x'))
                    ans += size*mult
                    multtoken = ''
                    i += size+1
            else:
                if letter == '(':
                    updatingmult = True
                else:
                    ans += 1
                i += 1
        
print('Answer:')
print(ans)

print('Answer part 2:')
print(ans2)

print('Total duration is', time.time() - start)