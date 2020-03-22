import sys
import itertools
from collections import Counter
sys.setrecursionlimit(10**8)
if __name__ == "__main__":
    N = int(input())
    A = input().split()
    counter = Counter(A)
    result = 0
    for c in counter.values():
        result += c*(c-1)//2
    for a in A:
        k = counter[a]
        print(result - k*(k-1)//2 + (k-1)*(k-2)//2)