def MI(): return map(int, input().split())

def calc(N, Y):
    for x in range(N+1):
        for y in range(N-x+1):
            z = N-x-y
            if 0<= z <= 2000 and 10000*x + 5000*y + 1000*z == Y:
                return (x, y, z)
    return (-1, -1, -1)

if __name__ == "__main__":
    N, Y = MI()
    (_10000, _5000, _1000) = calc(N, Y)
    print(_10000, _5000, _1000)