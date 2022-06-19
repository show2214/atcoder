W, N, *LRV = map(int, open(0).read().split())

d = [[0, 0]] + [[] for _ in range(W)]

for i in range(N):
    l, r, v = LRV[i*3:-~i*3]
    for j in range(W, l-1, -1):
        if d[j-l]:
            if []==d[j] or d[j-l][0]+v > d[j][0]:
                d[j] = [d[j-l][0]+v, d[j-l][1]+r]

a=[-1]

for x in d:
    if [] != x:
        v, r = x
        if r >= W:
            a += v,

print(max(a))