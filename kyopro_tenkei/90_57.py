N, M = map(int, input().split())
T = [0] * N
A = []

for i in range(N):
    input()
    for j in map(int, input().split()):
        T[i] |= 1 << j-1

S = sum(s << i for i, s in enumerate(map(int, input().split())))
p = 0

for i in range(M):
    a = 0
    for j in range(p, N):
        if T[j] >> i & 1:
            if j != p:
                T[j], T[p] = T[p], T[j]
            a = 1
            break
    if a:
        for j in range(N):
            if j != p and T[j] >> i & 1:
                T[j] ^= T[p]
        if S >> i & 1:
            S ^= T[p]
        p += 1

print(pow(2, N-p, 998244353) * (S<1))