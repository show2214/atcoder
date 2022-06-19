N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
mod = 10**9 + 7

ans = 1
for dices in A:
    ans *= sum(dices)
    ans %= mod

print(ans)