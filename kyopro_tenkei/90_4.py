# import numpy as np

# H, W = map(int,input().split())
# A = [list(map(int, input().split())) for l in range(H)]

# result = np.zeros((H, W), dtype=np.int32)
# row = np.sum(A, axis=1)
# column = np.sum(A, axis=0)

# for i in range(H):
#     for j in range(W):
#         # 行の分を全部足して列の分を後で足して重複してる分を引く
#         result[i][j] += row[i] + column[j] - A[i][j]

# for r in result:
#     print(*r)

H, W = map(int,input().split())
A = [list(map(int, input().split())) for l in range(H)]
row = []
column = []

for i in range(H):
    row.append(sum(A[i]))

for j in range(W):
    tmp = 0
    for i in range(H):
        tmp += A[i][j]
    column.append(tmp)

for i in range(H):
    for j in range(W):
        tmp = A[i][j]
        A[i][j] = row[i] + column[j] - tmp

for a in A:
    print(*a)