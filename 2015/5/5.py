import time
timestart = time.time()
file = "5/smallinput.txt"
file = "5/biginput.txt"

ans1 = 0
ans2 = 0

with open(file, 'r') as inputfile:
    filelines = inputfile.readlines()
    vowels = ('a', 'e', 'i', 'o', 'u')
    part1bad = ('ab', 'cd', 'pq', 'xy')
    for line in filelines:
        a = line.strip()
        # print('aaaaaaaaa', a)
        needs = [False, True]
        vc = 0
        for i in range(len(a)-1):
            if a[i] in vowels:
                vc += 1
            if a[i] == a[i+1]:
                needs[0] = True
            if a[i:i+2] in part1bad:
                needs[1] = False
                break
        if a[-1] in vowels:
            vc += 1
        # print(needs)
        if vc >= 3 and needs[0] and needs[1]:
            # print(a, 'is nice')
            ans1 += 1
        pos = {}
        doubledouble = False
        mitm = False
        for i in range(len(a)):
            if i < len(a) - 2 and a[i] == a[i+2]:
                mitm = True
            if i < len(a) - 1:
                pair = a[i:i+2]
                if pair in pos:
                    if pos[pair] < i - 1:
                        doubledouble = True
                else:
                    pos[pair] = i
            if doubledouble and mitm:
                ans2 += 1
                break

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)