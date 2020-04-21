def swap(A, B):
    return (B, A)

if __name__ == "__main__":
    X, Y, Z = input().split()
    X, Y = swap(X, Y)
    X, Z = swap(X, Z)
    print(X, Y, Z)