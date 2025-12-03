import time
start = time.time()
# file = "1/smallinput.txt"
file = "1/biginput.txt"
val = 50
zerocounter = 0
secondzerocounter = 0
with open(file, 'r') as inputfile:
    for line in inputfile.readlines():
        a = line.strip()
        if a[0] == 'L':
            leftturns = int(a[1:])
            if leftturns >= val and val != 0:
                leftturns -= val
                val = 0
                secondzerocounter += 1
            while leftturns > 0:
                if leftturns >= 100:
                    leftturns -= 100
                    secondzerocounter += 1
                else:
                    val = (val - leftturns)%100
                    break
        else:
            val = val+int(a[1:])
            if val >= 100:
                secondzerocounter += val//100
                val = val % 100
        if val < 0 or val > 99:
            print('error')
        if val == 0:
            zerocounter += 1

print('Final answer is:')
print(zerocounter)
print(secondzerocounter)
print('Total duration is', time.time() - start)