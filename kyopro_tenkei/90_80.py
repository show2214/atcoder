N, D = map(int, input().split())
A = list(map(int, input().split()))

B = [sum((A[j] >> i & 1) << j for j in range(N)) for i in range(D)]
dp = [1] + [0] * 2 ** N

for T in B:
    for S in range(2**N)[::-1]:
        dp[S|T] += dp[S]

print(dp[-2])