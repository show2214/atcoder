N, K, P = map(int, input().split())
A = [*map(int, input().split())]
a, b = A[:N//2], A[N//2:]
e = [[] for _ in range(K + 1)]

from bisect import *
from itertools import *

for i in range(K + 1):
    for t in combinations(a, i):
        e[i] += sum(t),

*e, = map(sorted, e)
c = 0

for i in range(K + 1):
    for t in combinations(b, i):
        s = sum(t)
        c += bisect(e[K - i], P - s)

print(c)