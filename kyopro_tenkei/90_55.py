N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] %= P

ans = 0

for i in range(N):
    for j in range(i+1, N):
        ij = A[i] * A[j] % P
        for k in range(j+1, N):
            ijk = A[k] * ij % P
            for l in range(k+1, N):
                ijkl = A[l] * ijk % P
                for m in range(l+1, N):
                    if A[m] * ijkl % P == Q:
                        ans += 1

print(ans)