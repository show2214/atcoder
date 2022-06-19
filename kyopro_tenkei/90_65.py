import numpy as np

R, G, B, K = map(int, input().split())
X, Y, Z = map(int, input().split())
MOD = 998244353

def convolve(a, b):
    fft_len = 1
    while 2*fft_len < len(a) + len(b) - 1:
        fft_len *= 2
    fft_len *= 2
    Fa = np.fft.rfft(a, fft_len)
    Fb = np.fft.rfft(b, fft_len)
    Fc = Fa * Fb
    c = np.fft.irfft(Fc, fft_len)
    c = np.rint(c).astype(np.int64)
    return c[:len(a) + len(b) -1]

def convolve_mod(a, b, p):
    a = np.array(a, np.int64)
    b = np.array(b, np.int64)

    a1, a2 = np.divmod(a, 1 << 15)
    b1, b2 = np.divmod(b, 1 << 15)

    x = convolve(a1, b1) % p
    z = convolve(a2, b2) % p
    y = (convolve(a1+a2, b1+b2)-(x+z)) % p

    c = (x << 30) + (y << 15) + z
    return c % p

m = 200001
fac = [1] * m
ninv = [1] * m
finv = [1] * m

for i in range(2, m):
    fac[i] = fac[i-1] * i % MOD
    ninv[i] = (-(MOD//i) * ninv[MOD%i]) % MOD
    finv[i] = finv[i-1] * ninv[i] % MOD

def comb(n, k):
    if k > n:
        return 0
    return (fac[n] * finv[k] % MOD) * finv[n - k] % MOD

a = [0] * (B + 1)

for i in range(K - X, B + 1):
    a[i] = comb(B, i)

b = [0] * (R + 1)

for i in range(K - Y, R + 1):
    b[i] = comb(R, i)

c = [0] * (G + 1)

for i in range(K - Z, G + 1):
    c[i] = comb(G, i)

print(convolve_mod(a, convolve_mod(b, c, MOD), MOD)[K])