N, K = map(int, input().split())
S = []

for i in range(N):
    a, b = map(int, input().split())
    S += [b, a-b]
print(sum(sorted(S)[-K:]))