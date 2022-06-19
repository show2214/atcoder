from networkx import *

N, W = map(int, input().split())
A = list(map(int, input().split()))
h = [list(map(int, input().split())) for _ in range(N)]

G = DiGraph()
f = G.add_edge

i = r = 0

for k, *c in h:
    i += 1
    f(0, i, c=A[i-1])
    f(i, f, c=W)
    [f(c, i) for c in c]

print(sum(A) - minimum_cut(G, 0, f, 'c')[0])