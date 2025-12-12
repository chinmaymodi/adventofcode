'''
So
basic single loop search takes about 1.5-2 seconds for part1 + part2 on this machine
Threading takes ~1.5 seconds
MultiProcessing takes ~12.5 seconds, idk why
ProcessPoolExecutor takes ~0.8 seconds
I think default python is cursed. Apparently, hashes in python happen at
500k - 1M per second. So the hard limit is near 1 second.
So 0.8 with ProcessPoolExecutor is very good for me.
'''
import time
timestart = time.time()
from hashlib import md5
file = "4/smallinput.txt"
file = "4/biginput.txt"

ans1 = 0
ans2 = 0

with open(file, 'r') as inputfile:
    filelines = inputfile.readlines()
    for line in filelines:
        a = line.strip()
        i = 0
        while True:
            md5hash = md5((a+str(i)).encode()).hexdigest()
            if md5hash.startswith('00000'):
                if ans1 == 0:
                    ans1 = i
                if ans2 == 0 and md5hash[5] == '0':
                    ans2 = i
                    break
            i += 1

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)