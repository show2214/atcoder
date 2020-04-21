if __name__ == "__main__":
    S = input()
    if len(S) != 6 or S[2] != S[3] or S[4] != S[5]:
        print("No")
    else:
        print("Yes")