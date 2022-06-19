from math import gcd

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
XY.sort()

def calc(a,b,c):
    x1, y1 = XY[a]
    x2, y2 = XY[b]
    x3, y3 = XY[c]
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

l = []
for i in range(N):
    while len(l) > 1 and calc(l[-2],l[-1],i)<=0:
        l.pop()
    l.append(i)

l2 = []
for i in range(N):
    while len(l2) > 1 and calc(l2[-2], l2[-1], i) >= 0:
        l2.pop()
    l2.append(i)
 
l += l2[1:-1][::-1]
XY.append((0, 0))
s, b = 0, 0
 
for i in range(len(l)):
    s+=calc(N, l[i], l[(i+1) % len(l)])
    b+=gcd(abs(XY[l[i]][0] - XY[l[(i + 1) % len(l)]][0]), abs(XY[l[i]][1] - XY[l[(i + 1) % len(l)]][1]))
ans = s + b + 2
print(ans // 2 - N)