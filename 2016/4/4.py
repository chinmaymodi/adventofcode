import time
start = time.time()
from collections import Counter
filename = "4/input.txt"
# filename = "4/smalltest.txt"

sectorsum = 0

def decode(encryptedname: str, sectorid: int):
    sectoridcopy = sectorid
    decryptedname = ''
    sectorid = sectorid % 26
    for letter in encryptedname:
        if letter == '-':
            decryptedname += ' '
            continue
        ordnewletter = ord(letter) + sectorid
        if ordnewletter > ord('z'):
            ordnewletter -= 26
        decryptedname += chr(ordnewletter)
    if 'North' in decryptedname or 'north' in decryptedname:
        print(decryptedname, sectoridcopy)
        # input()
    return decryptedname

with open(filename, 'r') as inputfile:
    for line in inputfile:
        tokens = line.strip().split('-')
        encname = '-'.join(tokens[:-1])
        encCounter = Counter(c for c in encname if c != '-')
        top5 = ''.join(sorted(encCounter, key=lambda k: (-encCounter[k], k))[:5])
        lastsplit = tokens[-1].split('[')
        # print(lastsplit)
        sectorid = int(lastsplit[0])
        checksum = lastsplit[1][:-1]
        # print(checksum, top5)
        if checksum == top5:
            sectorsum += sectorid
        decode(encname, sectorid)
print('Answer:')
print(sectorsum)
print('Total duration is', time.time() - start)