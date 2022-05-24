N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N):
    if A[i] != B[i]:
        diff = abs(A[i] - B[i])
        if diff > K:
            print("No")
            exit()
        else:
            K -= diff
if K % 2 == 0:
    print("Yes")
else:
    print("No")