if __name__ == "__main__":
    move = []
    current = (0, 0, 0)
    count = 0
    N = int(input())
    for _ in range(N):
        point = tuple(map(int, input().split()))
        if abs(point[1] - current[1]) + abs(point[2] - current[2]) <= abs(point[0] - current[0]) and point[0]%2 == (point[1] + point[2])%2:
            count += 1
        current = point
    print("Yes" if count==N else "No")