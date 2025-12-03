import time
timestart = time.time()
# file = "2/smallinput.txt"
file = "2/biginput.txt"

global ans1
ans1 = 0
global ans2
ans2 = 0
low, high = 0, 0

def part1(low, high) -> None:
    global ans1
    lenlow = len(str(low))
    half_len = lenlow // 2
    start = int(str(low)[:half_len])
    end = int(str(high)[:half_len]) + 1

    for i in range(start, end):
        si = str(i)
        z = int(si + si)
        if low <= z <= high:
            ans1 += z

def part2(low, high) -> None:
    seen = set()
    lenlow = len(str(low))
    lenhigh = len(str(high))
    limit = high // (10 ** (lenhigh // 2))
    global ans2

    for start in range(1, limit + 1):
        s = str(start)
        lens = len(s)
        zs = s * ((lenlow + lens - 1) // lens)
        lzs = len(zs)

        while lzs <= lenhigh:
            z = int(zs)
            if z in seen:
                break
            seen.add(z)
            if low <= z <= high:
                ans2 += z
            zs += s
            lzs += lens

with open(file, 'r') as inputfile:
    for line in inputfile.readlines():
        a = line.strip()
        for ranges in a.split(','):
            lowstr, highstr = ranges.split('-')
            lenlow = len(lowstr)
            lenhigh = len(highstr)
            if lenlow % 2:
                low = int('1' + ('0'*lenlow))
                lenlow += 1
            else:
                low = int(lowstr)
            if lenhigh % 2:
                high = int('9'*(lenhigh-1))
                lenhigh -= 1
            else:
                high = int(highstr)
            
            part2(int(lowstr), int(highstr))
            if low > high:
                continue
            part1(low, high)

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)