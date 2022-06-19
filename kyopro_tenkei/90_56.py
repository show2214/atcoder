N, S = map(int, input().split())
d = ['Impossible'] * 10 ** 5

for i in range(N):
    a, b = map(int, input().split())
    if i == 0:
        d[a-1] = 'A'
        d[b-1] = 'B'
    else:
        for j in range(10**5-1, -1, -1):
            d[j] = d[j-a] + 'A' if j >= a and d[j-a] != 'Impossible' else d[j-b] + 'B' if j >= b and d[j-b] != 'Impossible' else 'Impossible'

print(d[S-1])