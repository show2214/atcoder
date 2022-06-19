import sys
sys.setrecursionlimit(10**6)

N = int(input())
branch = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    branch[a - 1] += [b - 1]
    branch[b - 1] += [a - 1]

s = 0

def dfs(v, p=-1):
    global s
    r = 1
    for c in branch[v]:
        if c != p:
            r += dfs(c, v)
    s += r * (N - r)
    return r

dfs(0)
print(s)