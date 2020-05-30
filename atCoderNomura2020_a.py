if __name__ == "__main__":
    h1, m1, h2, m2, k = map(int, input().split())
    wake = h1*60+m1
    sleep = h2*60+m2
    print(sleep-wake-k)