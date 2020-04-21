import collections

def MI(): return map(int, input().split())
def LI(): return list(MI())

if __name__ == "__main__":
    N = int(input())
    A = dict(collections.Counter(LI()))
    for i in range(1, N+1):
        count = A.get(i)
        print(count if count is not None else 0)