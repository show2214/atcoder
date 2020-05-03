if __name__ == "__main__":
    X = int(input())
    for i in range(-119, 120):
        for j in range(-118, 119):
            if i ** 5 - j ** 5 == X:
                print(i, j)
                exit()