N, K = map(int, input().split())
MOD = 10 ** 9 + 7

if N == 1:
    ans = K
elif N == 2:
    ans = K * (K - 1)
else:
    ans = K * (K - 1) * pow((K - 2), (N - 2), MOD)

print(ans % MOD)