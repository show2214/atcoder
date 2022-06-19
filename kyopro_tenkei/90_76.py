N = int(input())
A = list(map(int, input().split()))
s = sum(A)
t = s - A[0]
f = l = 1

for r in A:
    t += r
    while t * 10 > s:
        t -= A[l % N]
        l += 1
    f &= t * 10 < s

print('YNeos'[f::2])