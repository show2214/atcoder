H, W = map(int, input().split())
C = [input() for _ in range(H)]

def f(x, y, a, b, l, s):
    if x == a and y == b and l > 2:
        return l
    elif not (0 <= x < H and 0 <= y < W) or C[x][y] == '#' or (x, y) in s:
        return -1
    else:
        return max(f(i, j, a, b, l + 1,s | {(x, y)}) for i, j in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)])

print(max(f(i, j, i, j, 0, set()) for i in range(H) for j in range(W)))