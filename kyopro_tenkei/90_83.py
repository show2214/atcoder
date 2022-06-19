(N,M),*Q=[[*map(int,s.split())]for s in open(0)]
E=Q[:M]
d=[0]*-~N
*T,=d
*U,=d
for a,b in E:
    d[a]+=1
    d[b]+=1
G=[[]for _ in d]
for a,b in E:
    if d[a]>d[b]:
        a,b=b,a
    G[a]+=b,
C=[1]
for x,y in Q[M+1:]:
    t=T[x]
    T[x]=U[x]=i=len(C)
    C+=y,
    for v in G[x]:
        t=max(t,U[v])
        T[v]=i
    print(C[t])