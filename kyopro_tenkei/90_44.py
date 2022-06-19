N, Q = map(int, input().split())
p = list(map(int, input().split()))
T = []

for _ in range(Q):
    t, x, y = map(int, input().split())
    T.append((t, x-1, y-1))

shift = 0
for t, x, y in T:
    X = (x - shift) % N
    Y = (y - shift) % N
    if t == 1:
        p[X], p[Y] = p[Y], p[X]
    elif t == 2:
        shift += 1
    else:
        print(p[X])
