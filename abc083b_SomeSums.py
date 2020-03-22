def MI(): return map(int, input().split())

def calc(N, A, B):
    result = []
    for x in range(1, N+1):
        tmp = list(map(int, list(str(x))))
        if A <= sum(tmp) <= B:
            result.append(x)
    return sum(result)

if __name__ == "__main__":
    (N, A, B) = MI()
    print(calc(N, A, B))