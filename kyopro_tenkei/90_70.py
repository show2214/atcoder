N = int(input())
X = []
Y = []

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

X.sort()
Y.sort()
Xm = X[N//2]
Ym = Y[N//2]

print(sum(abs(X[i] - Xm) + abs(Y[i] - Ym) for i in range(N)))