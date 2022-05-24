N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

inconvinience = 0

for i in range(N):
    inconvinience += abs(A[i]-B[i])

print(inconvinience)