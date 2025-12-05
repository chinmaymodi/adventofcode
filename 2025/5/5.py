import time
timestart = time.time()
import bisect
file = "5/smallinput.txt"
file = "5/biginput.txt"

ans1 = 0
ans2 = 0
with open(file, 'r') as inputfile:
    intervals = []
    for line in inputfile.readlines():
        a = line.strip()
        if len(a) == 0:
            continue
        if '-' in a:
            new_interval = list(map(int, a.split('-')))
            pos = bisect.bisect_left(intervals, new_interval)
            intervals.insert(pos, new_interval)
            if pos > 0 and intervals[pos-1][1] >= intervals[pos][0]:
                intervals[pos-1][1] = max(intervals[pos-1][1], intervals[pos][1])
                intervals.pop(pos)
                pos -= 1
            while pos+1 < len(intervals) and intervals[pos][1] >= intervals[pos+1][0]:
                intervals[pos][1] = max(intervals[pos][1], intervals[pos+1][1])
                intervals.pop(pos+1)
        else:
            a = int(a)
            pos = bisect.bisect_left(intervals, [a, a])
            isFresh = False
            
            if pos < len(intervals) and intervals[pos][0] <= a <= intervals[pos][1]:
                isFresh = True
            elif pos > 0 and intervals[pos-1][0] <= a <= intervals[pos-1][1]:
                isFresh = True
            
            if isFresh:
                ans1 += 1
    for i in intervals:
        ans2 += i[1] - i[0] + 1
        
    

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)