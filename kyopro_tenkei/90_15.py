N = int(input())

p = 10 ** 9 + 7
l = [1]

for i in range(1, N+1):
    l.append(l[-1] * i % p)

ll = [pow(i, -1, p) for i in l]
comb_mod = lambda n, r: l[n] * ll[r] * ll[n-r] % p
lll = [sum(comb_mod(N - (k-1) * i, i + 1) for i in range((N-1) // k + 1)) % p for k in range(1, N+1)]

for i in lll:
    print(i)