if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    print(sum([500*i+100*j+50*k==X for i in range(A+1) for j in range(B+1) for k in range(C+1)]))