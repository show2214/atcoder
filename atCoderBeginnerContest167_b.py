def MI(): return map(int, input().split())

if __name__ == "__main__":
    A, B, C, K = MI()
    tmp = K
    result = 0
    if K > A:
        tmp -= A
        result += A
    else:
        print(K)
        exit()
    if tmp > B:
        tmp -= B
    else:
        print(result)
        exit()
    print(result - tmp)