import sys
sys.setrecursionlimit(10 ** 7)

N, M, K = map(int, input().split())
G = [[] for _ in range(N)]
C = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    C[b] += 1

V = [0] * N
r = 0

for i in range(N):
    if C[i] == 0:
        V[r] = i
        r += 1

L = []
c = 0

def dfs(l, r):
    global c
    if l == N:
        L.append(list(V))
        if len(L) == K:
            for P in L:
                print(*[p + 1 for p in P])
            exit()
    for i in range(l, r):
        if i > l:
            if c == K:
                break
            c += 1
        V[l], V[i] = V[i], V[l]
        for nv in G[V[l]]:
            C[nv] -= 1
            if C[nv] == 0:
                V[r] = nv
                r += 1
        dfs(l + 1, r)
        for nv in G[V[l]]:
            if C[nv] == 0:
                r -= 1
            C[nv] += 1
        V[l], V[i] = V[i], V[l]

dfs(0, r)
print(-1)   