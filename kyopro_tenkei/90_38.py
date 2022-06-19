import math

A, B = map(int, input().split())
res = A * B // math.gcd(A, B)
if res > 1e18:
    print("Large")
else:
    print(res)