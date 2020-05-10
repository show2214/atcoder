def MI(): return map(int, input().split())
def LI(): return list(MI())
if __name__ == "__main__":
    N, M, X = MI()
    C = [LI() for _ in range(N)]
    ans = float('inf')
    for i in range(1<<N):
        score = [0] * M
        money = 0
        for j in range(N):
            if (1<<j) & i != 0:
                money += C[j][0]
                for k in range(M):
                    score[k] += C[j][k+1]
        if min(score) >= X:
            ans = min(ans, money)
    print(ans if ans != float('inf') else -1)
