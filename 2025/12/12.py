import time
timestart = time.time()

file = "12/smallinput.txt"
file = "12/biginput.txt"

ans1 = 0
ans2 = 0

shapesarea = []

with open(file, 'r') as inputfile:
    filelines = inputfile.readlines()
    i = 0
    while i < len(filelines):
        a = filelines[i].strip()
        if not a:
            i += 1
            continue
        if ':' in a:
            # either shape id or a container
            l, r = a.split(':')
            if r:
                #container
                w, h = map(int, l.split('x'))
                counts = list(map(int, r.strip().split()))
                if sum(shapesarea[i]*counts[i] for i in range(len(shapesarea))) <= w*h\
                    and w//3 * h//3 >= sum(counts):
                        ans1 += 1
                i += 1
            else:
                #shape
                filledarea = 0
                i += 1
                shapeline = filelines[i].strip()
                while shapeline:
                    filledarea += shapeline.count('#')
                    i += 1
                    shapeline = filelines[i].strip()
                shapesarea.append(filledarea)
                i += 1
                
print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)