H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]
q = 0

for S in range(2**H):
    d = {0:0}
    for j in range(W):
        s = {P[i][j] for i in range(H) if S >> i & 1}
        if len(s) == 1:
            p = s.pop()
            d[p] = d.get(p, 0) + 1
    q = max(q, bin(S).count('1') * max(d.values()))

print(q)