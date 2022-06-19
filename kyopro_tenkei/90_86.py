N,Q=map(int,input().split())
X=[]
MOD=10**9+7

for i in range(Q):
    x,y,z,w=map(int, input().split())
    X+=[(2**x+2**y+2**z>>1,w)]

s=1
for d in range(60):
    s*=sum(all((x&S>0)==w>>d&1 for x,w in X) for S in range(2**N))

print(s%MOD)