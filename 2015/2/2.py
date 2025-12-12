import time
timestart = time.time()
file = "2/smallinput.txt"
file = "2/biginput.txt"

ans1 = 0
ans2 = 0

with open(file, 'r') as inputfile:
    filelines = inputfile.readlines()
    for line in filelines:
        a = line.strip()
        l, w, h = map(int, a.split('x'))
        ans1 += 2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)
        ans2 += 2*(l+w+h - max(l, w, h)) + (l*w*h)

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)