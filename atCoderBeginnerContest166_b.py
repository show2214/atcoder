if __name__ == "__main__":
    N, K = map(int, input().split())
    member = set()
    for _ in range(K):
        trash = input()
        member |= set(map(int, input().split()))
    print(N-len(member))