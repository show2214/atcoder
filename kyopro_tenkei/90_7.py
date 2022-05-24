import bisect
N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for _ in range(Q):
    b = int(input())
    tmp = bisect.bisect(A, b)
    print(min(abs(A[tmp-1]-b), abs(A[min(tmp, len(A)-1)]-b)))