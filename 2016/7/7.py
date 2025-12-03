import time
start = time.time()

filename = "7/input.txt"
# filename = "7/smalltest.txt"
# filename = "7/smalltest2.txt"

ans = 0
ans2 = 0

with open(filename, 'r') as inputfile:
    for line in inputfile:
        # input()
        line = line.strip()
        # print('aaa:', line)
        isouter = True
        token = ''
        isouterABBA = False
        isinnerABBA = False
        outerset = set()
        innerset = set()
        for letter in line:
            if letter == '[':
                for i in range(2, len(token)):
                    if i >= 3 and token[i] == token[i-3] and token[i-1] == token[i-2] and token[i] != token[i-1]:
                        isouterABBA = True
                    if token[i] == token[i-2] and token[i] != token[i-1]:
                        outerset.add((token[i-1], token[i]))
                isouter = False
                token = ''
            elif letter == ']':
                for i in range(2, len(token)):
                    if i >= 3 and token[i] == token[i-3] and token[i-1] == token[i-2] and token[i] != token[i-1]:
                        isinnerABBA = True
                    if token[i] == token[i-2] and token[i] != token[i-1]:
                        innerset.add((token[i], token[i-1]))
                isouter = True
                token = ''
            else:
                token += letter
        if token:
            if any(token[i] == token[i-3] and token[i-1] == token[i-2] and token[i] != token[i-1] for i in range(3, len(token))):
                isouterABBA = True
            for i in range(2, len(token)):
                if token[i] == token[i-2] and token[i] != token[i-1]:
                    outerset.add((token[i-1], token[i]))
        if isouterABBA and not isinnerABBA:
            ans += 1
        if innerset & outerset:
            ans2 += 1
        
print('Answer:')
print(ans)

print('Answer part 2:')
print(ans2)

print('Total duration is', time.time() - start)