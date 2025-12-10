import time
timestart = time.time()
from itertools import combinations
from z3 import *
file = "10/smallinput.txt"
file = "10/biginput.txt"

ans1 = 0
ans2 = 0

def getxor(arr, target) -> int:
    n = len(arr)
    xorarray = [0] * (1 << n)
    for i in range(n):
        xorarray[1 << i] = arr[i]
    for k in range(1, n+1):
        for idxs in combinations(range(n), k):
            mask = 0
            for i in idxs:
                mask |= 1 << i
            if xorarray[mask] == 0:
                lsb = mask & -mask
                i = lsb.bit_length() - 1
                prev = mask ^ lsb
                xorarray[mask] = arr[i] ^ xorarray[prev]
            if xorarray[mask] == target:
                return k
    return -1

def min_presses_sum_z3(arr, target) -> int:
    m = len(target)
    vecs = [[(a >> j) & 1 for j in range(m)] for a in arr]
    x = [Int(f"x{i}") for i in range(len(arr))]
    s = Optimize()
    for xi in x:
        s.add(xi >= 0)
    for j in range(m):
        s.add(Sum([vecs[i][j] * x[i] for i in range(len(arr))]) == target[j])
    s.minimize(Sum(x))
    if s.check() == sat:
        return sum(s.model()[xi].as_long() for xi in x)
    else:
        return -1

with open(file, 'r') as inputfile:
    filelines = inputfile.readlines()
    for line in filelines:
        l = line.strip()
        target, rest = l.split(']')
        target = sum([2**(i-1) for i in range(len(target)) if target[i] == '#'])
        switches, joltages = rest.split('{')
        switches = switches.strip()
        arr = [ sum(1 << int(pos) for pos in token.strip("()").split(",")) 
                for token in switches.split()]
        # print(target, arr)
        min_size = getxor(arr, target)
        # print(min_size)
        ans1 += min_size
        joltages = tuple(map(int, joltages[:-1].split(',')))
        # print('in open file', joltages)
        ans2 += min_presses_sum_z3(arr, joltages)

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)