if __name__ == "__main__":
    X = int(input())
    A = X // 500 * 1000 + X % 500 // 5 * 5
    print(A)