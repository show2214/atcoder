N, M = map(int, input().split())
t = [[*map(int, input().split())] for _ in range(M)]
p = [-1] * N * 3
s = 1

f = lambda x: x * (p[x] < 0) or f(p[x])

for c, l, r in sorted(t):
    l, r = f(l), f(r + 1)
    if p[l] > p[r]:
        l, r = r, l
    if l - r:
        p[l] += p[r]
        p[r] = l
        s += c

print(s * (~N in p) - 1)