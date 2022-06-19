n = int(input())
LR = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n - 1):
    li, ri = LR[i]
    for j in range(i + 1, n):
        lj, rj = LR[j]
        count = max(0, min(li, rj + 1) - lj)
        tmp = count
        for k in range(max(li + 1, lj + 1), ri + 1):
            count = min(count + 1, rj - lj + 1)
            tmp += count
        ans += tmp/((ri - li + 1) * (rj - lj + 1))

print(ans)