from numpy import *
W,*AB=int_([*map(str.split,open(0))])
S=zeros([5001]*2)
for a,b in AB:S[a,b]+=1
c=cumsum
S=c(c(S,0),1)
t=W[1]+1
print(int_(S[:-t,:-t]-S[:-t,t:]-S[t:,:-t]+S[t:,t:]).max())