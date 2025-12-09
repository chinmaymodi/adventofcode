import time
timestart = time.time()
file = "9/smallinput.txt"
file = "9/biginput.txt"

ans1 = 0
ans2 = 0
reds = []
redreach = []
lr = 0
with open(file, 'r') as inputfile:
    filelines = inputfile.readlines()
    for line in filelines:
        l = line.strip()
        p1, p2 = map(int, l.split(','))
        reds.append([p1, p2])
        lr += 1
    for i in range(lr):
        x1 = reds[i][0]
        y1 = reds[i][1]
        for j in range(i + 1, lr):
            x2 = reds[j][0]
            y2 = reds[j][1]
            ans1 = max(ans1, abs(x1-x2+1)*abs(y1-y2+1))
    edges = [(reds[i], reds[(i+1) % lr]) for i in range(lr)]
    xs = sorted(set(p[0] for p in reds))
    ys = sorted(set(p[1] for p in reds))
    xmap = {v:i for i,v in enumerate(xs)}
    ymap = {v:i for i,v in enumerate(ys)}
    grid = [[0]*(len(xs)-1) for _ in range(len(ys)-1)]
    for yi in range(len(ys)-1):
        ymid = (ys[yi]+ys[yi+1])/2
        crossings = []
        for (x1,y1),(x2,y2) in edges:
            if y1==y2:
                continue
            if (y1<=ymid<y2) or (y2<=ymid<y1):
                xcross = x1 + (ymid-y1)*(x2-x1)/(y2-y1)
                crossings.append(xcross)
        crossings.sort()
        for k in range(0,len(crossings),2):
            xl,xr = crossings[k],crossings[k+1]
            for xi in range(len(xs)-1):
                if xs[xi]>=xl and xs[xi+1]<=xr:
                    grid[yi][xi]=1
    psum = [[0]*(len(xs)) for _ in range(len(ys))]
    for yi in range(len(ys)-1):
        for xi in range(len(xs)-1):
            psum[yi+1][xi+1]=grid[yi][xi]+psum[yi][xi+1]+psum[yi+1][xi]-psum[yi][xi]
    for i in range(lr):
        for j in range(i+1,lr):
            x1,y1=reds[i]
            x2,y2=reds[j]
            if x1==x2 or y1==y2: continue
            xa,xb=sorted([xmap[x1],xmap[x2]])
            ya,yb=sorted([ymap[y1],ymap[y2]])
            total=(xb-xa)*(yb-ya)
            inside=psum[yb][xb]-psum[ya][xb]-psum[yb][xa]+psum[ya][xa]
            if inside==total:
                area=(abs(x1-x2)+1)*(abs(y1-y2)+1)
                ans2=max(ans2,area)

print('Final answer is:')
print(ans1)
print(ans2)
print('Total duration is', time.time() - timestart)