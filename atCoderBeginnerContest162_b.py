if __name__ == "__main__":
    N = int(input())
    i = []
    for num in range(1, N+1):
        if num % 3 == 0 or num % 5 == 0:
            continue
        else:
            i.append(num)
    print(sum(i))