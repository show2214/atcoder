N = int(input())
g = [[] for _ in range(N)]
q = []
r = []
v = [0] * N

for i in range(N):
    a, b = map(int, input().split())
    g[a-1] += i,
    g[b-1] += i,
    if i+1 in (a, b):
        q += i,
        v[i] = 1
        r += i + 1,

while q:
    c = q.pop()
    for x in g[c]:
        if v[x] < 1:
            v[x] = 1
            r += x + 1,
            q += x,

if len(r) < N:
    r = [-1]

while r:
    print(r.pop())