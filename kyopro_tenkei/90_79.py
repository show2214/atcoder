H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
t = 0

for i in range(H - 1):
    for j in range(W - 1):
        s = B[i][j] - A[i][j]
        t += abs(s)
        A[i][j] += s
        A[i + 1][j] += s
        A[i][j + 1] += s
        A[i + 1][j + 1] += s

print(['No', f'Yes {t}'][A==B])