N, L = map(int, input().split())
mod = 10**9 + 7

s = [0] * (N + 1)
s[0] = 1

for i in range(1, N + 1):
    if i < L:
        s[i] = 1
    else:
        s[i] = s[i - 1] + s[i - L]

print(s[-1] % mod)