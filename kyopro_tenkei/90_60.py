N = int(input())
A = list(map(int, input().split()))
INF = 10**9
box = [INF] * (N+5)
pos = [-1] * (N+5)

from bisect import bisect_left

for i in range(N):
    num = bisect_left(box, A[i])
    box[num] = A[i]
    pos[i] = num + 1

A.reverse()
box2 = [INF] * (N+5)
pos2 = [-1] * (N+5)

for i in range(N):
    num = bisect_left(box2, A[i])
    box2[num] = A[i]
    pos2[i] = num + 1

ans = 0

for i in range(len(box)):
    ans = max(ans, pos[i] + pos2[N-1-i] -1)

print(ans)