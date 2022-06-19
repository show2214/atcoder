I=2**62
N,P,K=map(int, input().split())
G=[[*map(int, input().split())] for _ in range(N)]
def wf(x):
    d=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            d[i][j]=[G[i][j],x][G[i][j]<0]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return sum(i<j and d[i][j]<=P for i in range(N) for j in range(N))
if wf(0)<K or wf(I)>K:
    exit(print(0))
def bs(k,l=0,r=I):
    while r-l>1:
        m=r+l>>1
        if wf(m)<=k:
            r=m
        else:
            l=m
    return r
s=bs(K)
t=bs(K-1)
print(['Infinity',t-s][t<I])