def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = sorted(LI(), reverse=True)
    sum = sum(A)
    if A[M-1] < sum/(4*M):
        print("No")
    else:
        print("Yes")