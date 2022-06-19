import collections

def convert():
    return collections.Counter(map(lambda x: int(x) % 46, input().split()))

input()
A, B, C = convert(), convert(), convert()

print(sum(A[i] * B[j] * C[(-i-j) % 46] for i in A.keys() for j in B.keys()))