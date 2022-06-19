N,K=map(int,input().split())
A=list(map(int,input().split()))
U=sorted(set(A))
d={}
MOD=10**9+7
for i,u in enumerate(U):
    d[u]=i
A=[d[a] for a in A]
class BIT:
    def __init__(self,N):
        self.N=N
        self.data=[0]*(N+1)
        self.orig=[0]*N
    def add(self,i,x):
        self.orig[i]=(self.orig[i]+x)%MOD
        i+=1
        while i<=self.N:
            self.data[i]=(self.data[i]+x)%MOD
            i+=i&-i
    def sum(self,a,b):
        r=0
        i=b
        while i>0:
            r=(r+self.data[i])%MOD
            i-=i&-i
        i=a
        while i>0:
            r=(r-self.data[i])%MOD
            i-=i&-i
        return r
b=BIT(len(U))
d=BIT(N+1)
d.add(0,1)
k=l=0
for r in range(1,N+1):
    k+=b.sum(A[r-1]+1,len(U))
    b.add(A[r-1],1)
    while K<k and l<N:
        b.add(A[l],-1)
        k-=b.sum(0,A[l])
        l+=1
    d.add(r,d.sum(l,r))
print(d.orig[-1])