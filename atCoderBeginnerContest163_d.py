import sys
def MI(): return map(int, sys.stdin.readline().split())
if __name__ == "__main__":
    N, K = MI()
    result = 0
    mod = 10**9+7
    if N+1 == K:
        print(1)
    else:
        for i in range(K, N+2):
            result += i*(N-i+1)+1
        print(result%mod)