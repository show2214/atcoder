N, M = map(int, input().split())
l = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    l[a-1].append(b-1)
    l[b-1].append(a-1)

ANS = 0

for i in range(N):
    t = [j for j in l[i] if j < i]
    if len(t) == 1:
        ANS += 1

print(ANS)