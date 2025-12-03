import time
start = time.time()

filename = "6/input.txt"
# filename = "6/smalltest.txt"

message = ''
message2 = ''

with open(filename, 'r') as inputfile:
    counter = []
    for line in inputfile:
        word = line.strip()
        if counter == []:
            for l in word:
                counter.append(dict())
        for i in range(len(word)):
            counter[i][word[i]] = counter[i].get(word[i], 0) + 1
    for c in counter:
        # print(c)
        message += max(c, key=c.get)
        message2 += min(c, key=c.get)
        
        
print('Answer:')
print(message)

print('Answer part 2:')
print(message2)

print('Total duration is', time.time() - start)