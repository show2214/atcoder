if __name__ == "__main__":
    c = int(input())
    objs = []
    for _ in range(c):
        tmp = input()
        if not tmp in objs:
            objs.append(tmp)
    print(len(objs))