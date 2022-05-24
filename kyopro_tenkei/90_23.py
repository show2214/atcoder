H, W = map(int, input().split())
cells = [input() for _ in range(H)]
MOD = 10**9 + 7

from collections import defaultdict

lst = [0]
val = [1]

for i in range(H):
    for j in range(W):
        lst1 = []
        val1 = []
        for k, v in zip(lst, val):
            k //= 2
            if lst1 and lst1[-1] == k:
                val1[-1] = (val1[-1]+v)%MOD
            else:
                lst1.append(k)
                val1.append(v)
        
        mask = 6 if j == 0 else ((1<<W)|3) if j==W-1 else ((1<<W)|7)
        if cells[i][j] == ".":
            for k, v in zip(lst, val):
                if k&mask == 0:
                    k = (k//2) + (1<<W)
                    if lst1[-1] == k:
                        val1[-1] = (val1[-1]+v)%MOD
                    else:
                        lst1.append(k)
                        val1.append(v)
        lst, val = lst1, val1
print(sum(val)%MOD)