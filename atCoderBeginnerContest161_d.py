import sys

sys.setrecursionlimit(10 ** 6)

if __name__ == "__main__":
    K = int(input())
    result = []
    i = 1
    while(len(result) != K):
        tmp = list(map(int, str(i)))
        if len(tmp) == 1:
            result.append(str(i))
            i += 1
            continue
        for x in range(len(tmp)):
            if abs(int(tmp[x])-int(tmp[x+1])) <= 1 and x == len(tmp)-2:
                result.append(str(i))
                break
            elif abs(tmp[x]-tmp[x+1]) <= 1:
                continue
            else:
                break
        i += 1
    print(result[len(result)-1])