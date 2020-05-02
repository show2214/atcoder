if __name__ == "__main__":
    S = input()
    count = 0
    base = int("9"*200000)
    for i in range(base):
        tmp = 2019 * i
        if tmp < base:
            count = count + S.count(str(tmp))
        else:
            break
    print(count)