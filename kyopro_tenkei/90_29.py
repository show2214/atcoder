W, N = map(int, input().split())
bricks = []

def p1():
    B = [[] for _ in range(N+1)]
    l, r = bricks.pop()
    B[1].append((l, r))
    print(1)
    max_h = 1

    for _ in range(2, N+1):
        l, r = bricks.pop()
        h = 1
        for h1 in range(max_h, 0, -1):
            if h != 1:
                break
            for l1, r1 in B[h1]:
                if max(l, l1) > min(r, r1):
                    continue
                h = h1 + 1
                max_h = max(h, max_h)
                break
        B[h].append((l, r))
        print(h)

def p2():
    heights = [0] * (W+1)
    l, r = bricks.pop()
    for i in range(l, r+1):
        heights[i] = 1
    print(1)

    for _ in range(2, N+1):
        l, r = bricks.pop()
        h = 1
        for i in range(l, r+1):
            h = max(h, heights[i]+1)
        for i in range(l, r+1):
            heights[i] = h
        print(h)

length = 0
for _ in range(N):
    l, r = map(int, input().split())
    bricks.append((l, r))
    length += r - l

avg = length // N
bricks.reverse()

if avg < W // 100:
    p2()
else:
    p1()
