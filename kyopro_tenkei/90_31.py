dp = [[-1]*1400 for _ in range(60)]

def grundy(w, b):
    if dp[w][b] != -1:
        return dp[w][b]
    t = 0
    S = set()
    if w:
        S.add(grundy(w-1, b+w))
    if b >= 2:
        for i in range(-(-b//2), b):
            S.add(grundy(w, i))
    while t in S:
        t += 1
    dp[w][b] = t
    return t

n = int(input())
W = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
g = 0
for w, b in zip(W, B):
    g ^= grundy(w, b)
if g:
    print("First")
else:
    print("Second")