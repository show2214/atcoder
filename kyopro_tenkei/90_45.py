N, K = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]
INF = 10**18
SHIFT = 1 << N
dp = [[INF] * SHIFT for _ in range(K + 1)]
for bit in range(1, SHIFT):
    s = []
    for i in range(N):
        if (bit >> i) & 1:
            s.append(i)
    mx = 0
    for i in s:
        xi, yi = XY[i]
        for j in s:
            xj, yj = XY[j]
            d = (xi - xj) ** 2 + (yi - yj) ** 2
            mx = max(d, mx)
    dp[1][bit] = mx

for cnt in range(2, K + 1):
    for s in range(SHIFT):
        subset = (s - 1) & s
        while subset:
            dp[cnt][s] = min(dp[cnt][s], max(dp[cnt - 1][subset], dp[1][s - subset]))
            subset = (subset - 1) & s
print(dp[-1][-1])