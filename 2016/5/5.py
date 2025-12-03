import time
start = time.time()

from hashlib import md5

filename = "5/input.txt"
# filename = "5/smalltest.txt"

ans = ''
anspart2 = ''

def runhash(doorID:str):
    i = 0
    decoded = ''
    longerdecoded = ['!']*8
    longercharacters = 0
    while len(decoded) < 8 or longercharacters < 8:
        text = f"{doorID}{i}"
        hash = md5(text.encode()).hexdigest()
        if hash[:5] == '00000':
            position = hash[5]
            if len(decoded) < 8:
                decoded += position
            if position in '01234567':
                position = int(position)
                if longerdecoded[position] == '!':
                    longerdecoded[position] = hash[6]
                    longercharacters += 1
        i += 1
    return decoded, ''.join(longerdecoded)
with open(filename, 'r') as inputfile:
    line = inputfile.readline().strip()
    ans, anspart2 = runhash(line)
print('Answer:')
print(ans)
print('Answer Part 2:')
print(anspart2)
print('Total duration is', time.time() - start)