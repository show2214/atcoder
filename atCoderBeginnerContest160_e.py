def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

if __name__ == "__main__":
    X, Y, A, B, C = MI()
    p = LI()
    p.sort(reverse=True)
    q = LI()
    q.sort(reverse=True)
    pq = p[:X] + q[:Y] + LI()
    pq.sort(reverse=True)
    print(sum(pq[:X+Y]))