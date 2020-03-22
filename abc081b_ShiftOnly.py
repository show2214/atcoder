import sys
def II() : return int(sys.stdin.readline())
def LI() : return list(map(int, sys.stdin.readline().split()))

def div_count(l, count):
    notEven = list(filter(lambda tmp: tmp % 2 != 0, l))
    if len(notEven) == 0:
        count += 1
        count = div_count([x / 2 for x in l], count)
    else:
        print(count)

if __name__ == "__main__":
    N = II()
    l = LI()
    div_count(l, 0)