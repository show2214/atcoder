def BIT_add(tree, i, v):
    while i <= len(tree):
        tree[i - 1] += v
        i += -i & i

def BIT_sum(tree, r):
    v = 0
    while r > 0:
        v += tree[r - 1]
        r &= ~(-r & r)
    return v

N, M = map(int, input().split())
LR = sorted((list(map(int, input().split())) for i in range(M)), key=lambda x: (x[1], -x[0]))

tree = [0] * N
ans = 0

for l,r in LR:
    ans += BIT_sum(tree, l)
    BIT_add(tree, l + 1, 1)
    BIT_add(tree, r, -1)

print(ans)
