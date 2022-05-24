from numpy import *
N = int(input())
W = sorted([list(map(int, input().split())) for _ in range(N)])
P = zeros(5001, int)

for d, c, s in W:
    if c<=d:
        # 既にセットされている値と新しい値の大きいほうをセット
        P[c:d+1]=fmax(P[c:d+1], P[:d+1-c]+s)
# リストにセットされている値で一番大きいものを出力
print(amax(P))