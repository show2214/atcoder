if __name__ == "__main__":
    K = int(input())
    A, B = map(int, input().split())
    result = "NG"
    for i in range(A, B+1):
        if i % K == 0:
            result = "OK"
            break
    print(result)