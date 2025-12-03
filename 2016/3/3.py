import time
start = time.time()
smallfilename = "3/input.txt"

sidelengths = []
columnarlengths = []
validtriangles = 0
validcolumnartriangles = 0

with open(smallfilename, 'r') as inputfile:
    threelines = []
    for line in inputfile:
        templinearr = [int(i)  for i in line.strip().split(' ') if i != '']
        sidelengths.append(templinearr)
        threelines.append(templinearr)
        if len(threelines) == 3:
            # print(threelines)
            for i in range(3):
                tempcolarr = []
                for j in range(3):
                    tempcolarr.append(threelines[j][i])
                columnarlengths.append(tempcolarr)
            threelines = []
            # print(columnarlengths[:-3])
            # input()
print(len(columnarlengths) == len(sidelengths))
for a, b, c in sidelengths:
    if a+b > c and b+c > a and c+a > b:
        validtriangles += 1
for a, b, c in columnarlengths:
    if a+b > c and b+c > a and c+a > b:
        validcolumnartriangles += 1
print('Valid Triangles:')
print(validtriangles)
print('Valid Columnar Triangles:')
print(validcolumnartriangles)
print('Total Triangles:')
print(len(sidelengths))

print('Total duration is', time.time() - start)