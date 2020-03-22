if __name__ == "__main__":
    target = input()
    start = target[:int((len(target)-1)/2)]
    end = target[int((len(target)+3)/2)-1:]
    test = target[::-1]
    print("Yes" if target == target[::-1] and start == start[::-1] and end == end[::-1] else "No")