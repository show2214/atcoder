if __name__ == "__main__":
    S = input()
    T = input()
    print("Yes" if T.startswith(S) and len(T) == len(S)+1 else "No")