import numpy as np

mod = 10 ** 9 + 7

def mul(A, B, b, p):
    res = np.zeros(b, dtype=np.int64)
    BB = np.concatenate((B, B))
    for i in range(b):
        s = -i * p % b
        res += A[i] * BB[s:s + b] % mod
    return res % mod

N, B, K = map(int, input().split())
C = np.array(list(map(int, input().split())))
res = np.zeros(B, dtype=np.int64)
res[0] = 1
p = 10
a = np.zeros(B, dtype=np.int64)
for i in C:
    a[i % B] += 1
while N > 0:
    if N % 2 == 1:
        res = mul(res, a, B, p)
    a = mul(a, a, B, p)
    p = p * p % B
    N //= 2

print(res[0])