def MI(): return map(int, input().split())
def LI(): return list(MI())

if __name__ == "__main__":
    N, M = MI()
    H = LI()
    roots = []
    for _ in range(M):
        roots.append(LI())
    result = [True] * N
    for root in roots:
        if H[root[0]-1] > H[root[1]-1]:
            result[root[1]-1] = False
        elif H[root[0]-1] < H[root[1]-1]:
            result[root[0]-1] = False
        else:
            result[root[0]-1] = False
            result[root[1]-1] = False
    print(result.count(True))