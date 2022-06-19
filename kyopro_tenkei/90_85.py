K=int(input())
i=1
ans=0

while i**3<=K:
    if K%i==0:
        L=K//i
        j=i
        while j*j<=L:
            ans+=int(L%j==0)
            j+=1
    i+=1

print(ans)