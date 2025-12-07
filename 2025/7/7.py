import time
timestart = time.time()
file = "7/smallinput.txt"
file = "7/biginput.txt"

ans1 = 0
ans2 = 0
with open(file, 'r') as inputfile:
    filelines = inputfile.readlines()
    base = []
    base3 = []
    for line in filelines:
        newseen = set()
        l = line.strip()
        if not base:
            base = list(l)
            base3 = [0 for _ in range(len(l))]
        else:
            for i in range(len(l)):
                if base[i] == 'S':
                    base[i] = '|'
                    base3[i] += 1
                elif base[i] == '|':
                    if l[i] == '.':
                        base[i] = '|'
                    else:
                        tempnum = base3[i]
                        base3[i] = 0
                        if i > 0:
                            if base[i-1] != '|':
                                base[i-1] = '|'
                            base3[i-1] += tempnum
                        if i < len(l) - 1:
                            base[i+1] = '|'
                            base3[i+1] += tempnum
                        ans1 += 1
                        base[i] = '.'
    ans2 = sum(base3)
        
        
print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)