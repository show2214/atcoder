N = int(input())
S = []
tmp = input()

for s in tmp:
    if s == 'a':
        S.append(0)
    elif s == 'b':
        S.append(1)
    else:
        S.append(2)

ans = 0

for i, s in enumerate(S):
    ans += 2 ** i * s

print(ans)