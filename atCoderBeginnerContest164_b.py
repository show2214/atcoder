if __name__ == "__main__":
    A, B, C, D = map(int, input().split())
    print("Yes" if -(-A//D) >= -(-C//B) else "No")