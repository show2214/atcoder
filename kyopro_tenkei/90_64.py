N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [i - j for i, j in zip(A, A[1:])] + [0]
ans = sum(map(abs, B))

LRV = [tuple(map(int, input().split())) for _ in range(Q)]

for l, r, v in LRV:
    ans -= abs(B[l-2]) + abs(B[r-1])
    B[l-2] -= v * (l > 1)
    B[r-1] += v * (r < N)
    ans += abs(B[l-2]) + abs(B[r-1])
    print(ans)