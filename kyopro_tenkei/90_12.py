from networkx.utils import UnionFind

H, W = map(int, input().split())
Q = int(input())
P = set()
uf = UnionFind()

for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 1:
        x, y = (a-1 for a in q)
        P.add((x, y))
        for u, v in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            if (u, v) in P:
                uf.union((x, y), (u, v))
    else:
        xa, ya, xb, yb = (a-1 for a in q)
        if {(xa, ya), (xb, yb)}<=P and uf[(xa, ya)]==uf[(xb, yb)]:
            print("Yes")
        else:
            print("No")