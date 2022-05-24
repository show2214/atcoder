N, K = map(int, input().split())
S = list(input())[::-1]

res = []
while S:
    while res and res[-1]>S[-1] and len(res)+len(S)>K:
        res.pop()
    res.append(S.pop())
print("".join(res[:K]))
