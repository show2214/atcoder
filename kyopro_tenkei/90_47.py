N = int(input())
S, T = input(), input()

def convert(p):
    res = [0] * N
    for i in range(N):
        if p[i] == "G":
            res[i] = 1
        elif p[i] == "B":
            res[i] = 2
    return res

a = convert(S)
b = convert(T)

base = 3
mod = 10**9 + 7

def calc(x, y, i, m):
    cnt = 0
    hash1 = 0
    hash2 = 0
    tmp = 1
    for j in range(m):
        hash1 *= base
        hash1 += x[j]
        hash1 %= mod

        hash2 += tmp * ((i - y[N-1-j]) % 3)
        hash2 %= mod

        if hash1 == hash2:
            cnt += 1
        tmp *= base
        tmp %= mod
    return cnt

ans = 0

for i in range(3):
    ans += calc(a, b, i, N)
    ans += calc(b, a, i, N-1)

print(ans)