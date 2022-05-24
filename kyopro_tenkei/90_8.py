N = int(input())
S = input()
mod = 10**9+7
T="atcoder"
p=[0]*8
p[0]=1
for i in range(N):
	for j in range(7):
		if S[i]==T[j]:
			p[j+1]+=p[j]
			p[j+1]%=mod
print(p[7])