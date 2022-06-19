N = int(input())
C = input().split()
MOD = 10 ** 9 + 7
node = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    node[a-1].append(b-1)
    node[b-1].append(a-1)

def dfs(v, p):
    c1, c2 = 1, 1
    for nv in node[v]:
        if nv == p:
            continue
        t0, t1 = dfs(nv, v)
        if C[v] == C[nv]:
            c1 *= t0 + t1
        else:
            c1 *= t0
        c1 %= MOD
        c2 *= 2 * t0 + t1
        c2 %= MOD
    c0 = c2 - c1
    c0 %= MOD
    return c0, c1

import sys
sys.setrecursionlimit(10**7)

ans = dfs(0, -1)[0]

print(ans)