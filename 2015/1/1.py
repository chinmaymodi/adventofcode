import time
timestart = time.time()
file = "1/smallinput.txt"
file = "1/biginput.txt"

ans1 = 0
ans2 = 0

with open(file, 'r') as inputfile:
    for line in inputfile:
        a = line.strip()
        for i in range(len(a)):
            ans1 += 1 if a[i] == '(' else -1
            if ans1 == -1 and ans2 == 0:
                ans2 = i + 1

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)