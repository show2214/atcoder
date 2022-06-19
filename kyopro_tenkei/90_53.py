import sys

def Ask(n):
    if idx[n] == -1:
        print('? ' + str(n))
        t = int(input())
        idx[n] = t
        return t
    return idx[n]

T = int(input())
idx = [0] * 1609
fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

for i in range(T):
    N = int(input())
    ans = 0

    for j in range(N+1):
        idx[j] = -1
    for j in range(N+1, 1601):
        idx[j] = -j
    
    if (N <= 5):
        for j in range(1,1+N):
            ans = max(ans, Ask(j))
    else:
        cl = 0
        cr = 1597
        dl = 610
        dr = 987
        el = Ask(dl)
        er = Ask(dr)
        ans = max(ans, el, er)
        if el < er:
            cl = dl
            dl = dr
            dr = -1
            el = er
            er = -1
        else:
            cr = dr
            dr = dl
            dl = -1
            er = el
            el = -1
        for j in range(12,-1,-1):
            if (dl == -1):
                dl = cl + fib[j]
                el = Ask(dl);   
            elif (dr == -1):
                dr = cr - fib[j]
                er = Ask(dr)
            ans = max(ans, el, er)
            if el < er:
                cl = dl
                dl = dr
                dr = -1
                el = er
                er = -1
            else:
                cr = dr
                dr = dl
                dl = -1
                er = el
                el = -1
        for j in range(cl + 1, cr):
            ans = max(ans,Ask(j))
    print("! " + str(ans))
    sys.stdout.flush()