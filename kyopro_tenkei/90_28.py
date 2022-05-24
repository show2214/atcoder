N = int(input())

from numpy import *
P = zeros([1001]*2, 'i')

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    P[lx, ly] += 1
    P[lx, ry] -= 1
    P[rx, ly] -= 1
    P[rx, ry] += 1

for i in histogram(cumsum(cumsum(P, 0)), range(N+2))[0][1:]:
    print(i)