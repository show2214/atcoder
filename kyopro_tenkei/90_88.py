N,Q=map(int,input().split())
A=tuple(map(int,input().split()))
s=sum(A)
G=[set() for _ in range(N+1)]
for _ in range(Q):
    x,y=map(int,input().split())
    G[x].add(y)
    G[y].add(x)
dp=[set() for _ in range(s+1)]
dp[0].add(0)
for i,a in enumerate(A,1):
    for j in range(a,s+1)[::-1]:
        if not dp[j-a] or dp[j-a]&G[i]:
            continue
        X = dp[j-a] | {i}
        if dp[j]:
            dp[j].remove(0)
            X.remove(0)
            print(len(dp[j]))
            print(*sorted(dp[j]))
            print(len(X))
            print(*sorted(X))
            exit()
        dp[j]=X