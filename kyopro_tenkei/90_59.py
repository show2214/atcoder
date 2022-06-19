N, M, Q = map(int, input().split())
adj = [[] for _ in range(N)]

# 辺の向き先を設定
for i in range(M):
    x, y = map(int, input().split())
    adj[x-1].append(y-1)

# 頂点部分を初期値としてビットのかたちで設定
dp = [1 << i for i in range(N)]

# 各頂点からの辺の向き先をOR演算で更新
for i in range(N):
    for j in adj[i]:
        dp[j] |= dp[i]

# 更新した結果からYes/Noを出力
for _ in range(Q):
    a, b = map(int, input().split())
    print('Yes' if (dp[b-1] >> (a-1)) & 1 else 'No')