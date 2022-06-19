N, M = map(int, input().split())
g = [[] for _ in range(N + M)]

for i in range(M):
    input()
    for j in map(int, input().split()):
        g[N + i] += j - 1,
        g[j - 1] += N + i,

from collections import *
q = deque([0])
v = [0] + [-1] * (N + M)

while q:
    c = q.popleft()
    for b in g[c]:
        if v[b] < 0:
            v[b] = v[c] + 1
            q += b,

print(*[i//2 for i in v[:N]])