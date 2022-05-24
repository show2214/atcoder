N = int(input())
A = list(map(int, input().split()))

from functools import *

@lru_cache(None)
def f(l, r):
    res=abs(A[l]-A[r])
    if ~l+r:
        res+=f(l+1, r-1)
        for i in range(l+1, r-1, 2):
            res=min(res, f(l, i)+f(i+1, r))
    return res

print(f(0, N*2-1))