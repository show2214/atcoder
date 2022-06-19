L,R=map(int,input().split())
MOD=10**9+7
ans = 0
cnt = 0

while R>=L:
    ans+=((R*(R+1)-L*(L-1))//2)%MOD
    ans%=MOD
    cnt+=1
    L=max(10**cnt,L)

print(ans)