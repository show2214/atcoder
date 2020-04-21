def MI(): return map(int, input().split())

if __name__ == "__main__":
    N, K = MI()
    print(min(N%K, K-N%K))