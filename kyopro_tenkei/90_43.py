INF = 10**6
f=lambda:map(int,input().split())
H, W = f()
sx, sy = f()
sx -= 1
sy -= 1
gx, gy = f()
gx -= 1
gy -= 1
S = [input() for _ in range(H)]
C = [[INF] * W for _ in range(H)]
C[sx][sy] = 0

from collections import *

q = deque()

for dir in range(4):
    q.append((0, dir, sx, sy))

while q:
    c, d, x, y = q.popleft()
    if C[x][y] < c:
        continue
    for td in range(4):
        dx, dy = [(1, 0), (0, 1), (-1, 0), (0, -1)][td]
        tx, ty = x + dx, y + dy
        if 0 <= tx < H and 0 <= ty < W and S[tx][ty] == '.':
            if td == d:
                if C[tx][ty] >= c:
                    C[tx][ty] = c
                    q.appendleft((c, d, tx, ty))
            else:
                if C[tx][ty] > c:
                    C[tx][ty] = c + 1
                    q.append((c + 1, td, tx, ty))

print(C[gx][gy])