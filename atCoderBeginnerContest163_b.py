def MI(): return map(int, input().split())
def LI(): return list(MI())

if __name__ == "__main__":
    N, M = MI()
    A = sum(LI())
    print(N-A if N >= A else -1)