N, K = map(int, input().split())
if N == 0:
    print(N)
    exit()

MOD = 10 ** 5
s = {N}
arr = [N]
s_num = -1
x = N

for _ in range(K):
    s_num = len(s)
    y = sum([int(a) for a in str(x)])
    x = (x + y) % MOD
    s.add(x)
    if s_num == len(s):
        roop_start = arr.index(x)
        roop = len(s) - roop_start
        break
    arr.append(x)

else:
    roop_start = 0
    roop = 10 ** 5
    x = N

for _ in range((K - roop_start) % roop):
    y = sum([int(a) for a in str(x)])
    x = (x + y) % MOD

print(x)