N = int(input())
tree = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

order = [-1] * N
stack = [0]
par = [-1] * N
dep = [0] * N
cnt = 0

while stack:
    v = stack.pop()
    order[v] = cnt
    cnt += 1
    for c in tree[v]:
        if par[c] != -1 or par[v] == c:
            continue
        par[c] = v
        dep[c] = dep[v] + 1
        stack.append(c)

ht = (N-1).bit_length()
kpar = [par]
prev = par

for k in range(ht):
    now = [0] * N
    for i in range(N):
        if prev[i] == -1:
            continue
        now[i] = prev[prev[i]]
    kpar.append(now)
    prev = now

def lca(u, v, kpar, dep):
    d = dep[v] - dep[u]
    if d < 0:
        u, v, d = v, u, -d
    for par in kpar:
        if d & 1:
            v = par[v]
        d >>= 1
    if u == v:
        return u
    for par in kpar[::-1]:
        pu, pv = par[u], par[v]
        if pu != pv:
            u, v = pu, pv
    return kpar[0][u]

def dist(u, v, kpar, dep):
    l = lca(u, v, kpar, dep)
    d = dep[u] + dep[v] - 2 * dep[l]
    return d

Q = int(input())
for _ in range(Q):
    k, *v = map(int, input().split())
    v = [a - 1 for a in v]
    v.sort(key=lambda x: order[x])
    ans = 0
    for i in range(k):
        ans += dist(v[i-1], v[i], kpar, dep)
    ans //= 2
    print(ans)