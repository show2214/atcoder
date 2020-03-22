import itertools as it

if __name__ == "__main__":
    N, M = map(int, input().split())
    n = len(list(it.combinations(["0" for _ in range(N)], 2)))
    m = len(list(it.combinations(["0" for _ in range(M)], 2)))
    print(n+m)