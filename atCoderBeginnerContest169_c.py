if __name__ == "__main__":
    a, b = input().split()
    a = int(a)
    b = round(float(b)*100)
    print((a*b)//100)