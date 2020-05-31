from functools import reduce

def m(l):
    result = 1
    for num in l:
        result *= num
        if result == 0:
            return 0
        elif result > 10**18:
            return -1
    return result

if __name__ == "__main__":
    input()
    aList = list(map(int, input().split()))
    aList.sort()
    print(m(aList))