import time
timestart = time.time()
file = "6/smallinput.txt"
file = "6/biginput.txt"

ans1 = 0
ans2 = 0

with open(file, 'r') as inputfile:
    filelines = inputfile.readlines()
    for line in filelines:
        a = line.strip()

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)