N, K = map(int, input().split())
N += 1
d = [0] * N
z = 0
for i in range(2, N):
    j = d[i] * N
    while j < N:
        d[j] += 1
        j += i
    z += d[i] >= K
print(z)