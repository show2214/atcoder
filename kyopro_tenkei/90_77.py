from typing import List, Tuple
import sys

class BipartiteMatching:
    def __init__(self, n: int, m: int) -> None:
        self._n = n
        self._m = m
        self._to: List[List[int]] = [[] for _ in range(n)]
    
    def add_edge(self, a: int, b: int) -> None:
        self._to[a].append(b)
    
    def solve(self) -> List[Tuple[int, int]]:
        n, m, to = self._n, self._m, self._to
        pre = [-1] * n
        root = [-1] * n
        p = [-1] * n
        q = [-1] * m
        upd = True
        while upd:
            upd = False
            s = []
            s_front = 0
            for i in range(n):
                if p[i] == -1:
                    root[i] = i
                    s.append(i)
            while s_front < len(s):
                v = s[s_front]
                s_front += 1
                if p[root[v]] != -1:
                    continue
                for u in to[v]:
                    if q[u] == -1:
                        while u != -1:
                            q[u] = v
                            p[v], u = u, p[v]
                            v = pre[v]
                        upd = True
                        break
                    u = q[u]
                    if pre[u] != -1:
                        continue
                    pre[u] = v
                    root[u] = root[v]
                    s.append(u)
            if upd:
                for i in range(n):
                    pre[i] = -1
                    root[i] = -1
        return [(v, p[v]) for v in range(n) if p[v] != -1]

dir = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
N, T, *AB = map(int, sys.stdin.buffer.read().split())
A, B, BD = [], [], dict()

for i, xy in enumerate(zip(*[iter(AB)]*2)):
    if i < N:
        A.append(xy)
    else:
        B.append(xy)
        BD[xy] = i - N

G = BipartiteMatching(N, N)

for i, (x, y) in enumerate(A):
    for dx, dy in dir:
        bx = x + dx * T
        by = y + dy * T
        if (bx, by) in BD:
            bi = BD[(bx, by)]
            G.add_edge(i, bi)

match = G.solve()

if len(match) != N:
    print('No')
    exit()

print('Yes')
ans = [0] * N

for ai, bi in match:
    ax, ay = A[ai]
    bx, by = B[bi]
    for d, (dx, dy) in enumerate(dir):
        if bx != ax + dx * T:
            continue
        if by != ay + dy * T:
            continue
        ans[ai] = d + 1
        break

print(*ans)