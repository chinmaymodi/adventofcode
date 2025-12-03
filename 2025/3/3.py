import time
timestart = time.time()
file = "3/smallinput.txt"
file = "3/biginput.txt"

ans1 = 0
ans2 = 0
with open(file, 'r') as inputfile:
    for line in inputfile.readlines():
        # print(line)
        l = line.strip()
        a = max(l[:-1])
        b = int(max(l[l.index(a)+1:]))
        # print(a, b)
        ans1 += 10*int(a) + b
        p2val = ''
        start = 0
        for i in range(-11, 1):
            c = max(l[:i]) if i != 0 else max(l)
            p2val += c
            start = l.index(c)+1
            l = l[start:]
            # print(start, i, p2val, l)
        ans2 += int(p2val)

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)