N, B = map(int, input().split())

S = [set() for i in range(12)]
S[0] = set([1])
for i in range(11):
  for j in S[i]:
    for k in range(10):
      S[i + 1].add(j * k)

def f(num):
    res = 1
    while num:
        res *= num % 10
        num //= 10
    return res

count = 0

for i in S[11]:
    x = B + i
    if f(x) == i and x <= N:
        count += 1

print(count)