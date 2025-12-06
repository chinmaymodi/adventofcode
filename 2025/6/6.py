import time
timestart = time.time()
import operator
from functools import reduce
file = "6/smallinput.txt"
file = "6/biginput.txt"

ans1 = 0
ans2 = 0
with open(file, 'r') as inputfile:
    elements = []
    filelines = inputfile.readlines()
    for line in filelines[:-1]:
        a = line.strip()
        row = []
        for num in a.split(' '):
            if num:
                row.append(int(num))
        elements.append(row)
    elementscol = list(map(list, zip(*elements)))
    symbols = []
    for sym in filelines[-1].strip().split(' '):
        if sym:
            symbols.append(sym)
    # print(elements)
    # print(symbols)
    for i in range(len(symbols)):
        ans1 += reduce({'*': operator.mul, '+': operator.add}[symbols[i]], elementscol[i])
    elements = []
    maxlen = 0
    for line in filelines[:-1]:
        l = []
        for i in line:
            if i != '\n':
                l.append(i)
        elements.append(l)
        maxlen = max(maxlen, len(l))
    for row in elements:
        while len(row) < maxlen:
            row.append(' ')
    # print(elements)
    elementscol = [int("".join(ch for ch in col if ch.strip())) if "".join(ch for ch in col if ch.strip()) else -1 for col in zip(*elements)]
    numlist = []
    for num in elementscol[::-1]:
        if num != -1:
            numlist.append(num)
        else:
            sym = symbols.pop()
            ans2 += reduce({'*': operator.mul, '+': operator.add}[sym], numlist)
            numlist = []
    if numlist:
        sym = symbols.pop()
        ans2 += reduce({'*': operator.mul, '+': operator.add}[sym], numlist)
print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)