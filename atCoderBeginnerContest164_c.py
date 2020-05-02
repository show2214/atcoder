if __name__ == "__main__":
    N = int(input())
    l = []
    for i in range(N):
        l.append(input())
    print(len(set(l)))