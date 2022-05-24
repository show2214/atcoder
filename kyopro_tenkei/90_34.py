N, K = map(int, input().split())
A = list(map(int, input().split()))
D = {}
l = 0

for a in A:
    d = D.get(a, 0)
    D[a] = d + 1
    K -= (d < 1)
    if K < 0:
        d = D[A[l]]
        D[A[l]] = d - 1
        K += (d < 2)
        l += 1

print(N-l)
