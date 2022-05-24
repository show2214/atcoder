N = int(input())

c1 = [0]
c2 = [0]

c1s = 0
c2s = 0

for i in range(N):
    c, s = map(int, input().split())
    if c == 1:
        c1s += s
    else:
        c2s += s
    c1.append(c1s)
    c2.append(c2s)

Q = int(input())

for _ in range(Q):
    start, end = map(int, input().split())
    print(c1[end] - c1[start-1], c2[end] - c2[start-1])