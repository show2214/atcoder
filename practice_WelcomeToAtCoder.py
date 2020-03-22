import sys
def II() : return int(sys.stdin.readline())
def MI() : return map(int, sys.stdin.readline().split())

a = II()
(b, c) = MI()
s = input()

print(a+b+c, s)