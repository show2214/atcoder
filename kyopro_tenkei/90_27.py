N = int(input())

res = {}

for i in range(N):
    name = input()
    res.setdefault(name, i+1)

for day in sorted(res.values()):
    print(day)