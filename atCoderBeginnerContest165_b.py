if __name__ == "__main__":
    X = int(input())
    year = 0
    money = 100
    while money < X:
        year += 1
        money = int(money*1.01)
    print(year)