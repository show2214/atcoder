def solv(L, N, M, A):
    cnt = 0
    pre = 0
    for i in range(N):
        if A[i] - pre >= M and L - A[i] >= M:
            cnt += 1
            pre = A[i]
    if cnt >= K:
        return True
    return False

if __name__ == "__main__":
    N, L = map(int, input().split())
    K = int(input())
    A = list(map(int, input().split()))

    left = -1
    right = L + 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if solv(L, N, mid, A) == False:
            right = mid
        else:
            left = mid
    print(left)
