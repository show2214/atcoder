A, B, C = map(int, input().split())

def gcd(a, b):
    c = a % b
    while c != 0:
        a, b = b, c
        c = a % b
    return b

_gcd = min([gcd(A, B), gcd(B, C), gcd(A, C)])

print((A//_gcd-1)+(B//_gcd-1)+(C//_gcd-1))