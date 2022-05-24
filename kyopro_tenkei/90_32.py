N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
X = [tuple(map(int, input().split())) for _ in range(M)]

XY = {i: set() for i in range(N)}

for x, y in X:
    XY[x - 1].add(y - 1)

dp = [[{} for _ in range(N)] for _ in range(N)]
for j in range(N):
    mm = 1 << j
    dp[0][j][mm] = A[j][0]

for i in range(1, N):
    for j in range(N):
        mm = 1 << j
        for l in range(N):
            low = l if l < j else j
            high = j if l <= j else l
            if high in XY[low]:
                continue
            for k, v in dp[i - 1][l].items():
                if mm & k == 0:
                    vv = v + A[j][i]
                    if (mm | k) not in dp[i][j] or dp[i][j][mm | k] > vv:
                        dp[i][j][mm | k] = vv

answer = -1
for l in range(N):
    if len(dp[-1][l]) > 0:
        x = min(dp[-1][l].values())
        if answer == -1 or answer > x:
            answer = x
print(answer)