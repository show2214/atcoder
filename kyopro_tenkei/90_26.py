N = int(input())
Z = {i : set() for i in range(N)}

for i in range(N-1):
    A, B = (int(x)-1 for x in input().split())
    Z[A].add(B)
    Z[B].add(A)

res, val, queue = [[], []], set(), [(0, 0, -1)]

while queue:
    q, d, p = queue.pop()
    if q in val:
        continue
    val.add(q)
    res[d%2]+=[q+1]
    queue+=[(t, d+1, q) for t in Z[q] - {p}]

res.sort(key=len)
print(*res[1][:N//2])