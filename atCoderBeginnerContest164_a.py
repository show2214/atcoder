if __name__ == "__main__":
    S, W = map(int, input().split())
    print("unsafe" if S <= W else "safe")