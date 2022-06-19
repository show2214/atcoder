N, Q = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
QI = [int(input()) for _ in range(Q)]

L=[]
a=c=9e9
b=d=-a

for x, y in XY:
    x, y = x+y, x-y
    a = min(x, a)
    b = max(x, b)
    c = min(y, c)
    d = max(y, d)
    L.append((x, y))

for i in range(Q):
    x, y = L[QI[i]-1]
    print(max(x-a, b-x, y-c, d-y))