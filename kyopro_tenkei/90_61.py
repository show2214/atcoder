from collections import deque
Q = int(input())
tx = [tuple(map(int, input().split())) for _ in range(Q)]
result = deque()
for t, x in tx:
    if t == 1:
        result.appendleft(x)
    elif t == 2:
        result.append(x)
    elif t == 3:
        print(result[x-1])