N = int(input())
Q = int(input())
p = [-1] * N

def l(a):
    while p[a] >= 0:
        a = p[a]
    return a

def m(a, b):
    x, y = l(a), l(b)
    if x != y:
        p[x] += p[y]
        p[y] = x

S = [2] * Q
q = ['000'] * Q
A = [0] * N

for i in range(Q):
    t, x, y, v = map(int, input().split())
    x, y = x - 1, y - 1
    if t:
        S[i] = l(x) == l(y)
        q[i] = (x, y, v)
    else:
        m(x, y)
        A[y] = v

for i in range(1, N):
    A[i] -= A[i - 1]

for s, (x, y, v) in zip(S, q):
    if s < 1:
        print('Ambiguous')
    if s == 1:
        print(A[y] + (v - A[x]) * (-1) ** (x^y))