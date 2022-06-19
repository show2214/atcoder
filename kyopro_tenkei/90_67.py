N, K = input().split()
K = int(K)

def replace8to5(str_num):
    return str_num.replace('8', '5')

def convert8to10(str_num):
    ans = 0
    str_num = list(reversed(str_num))
    for i in range(len(str_num)):
        ans += int(str_num[i]) * (8 ** i)
    return str(ans)

def convert10to9(str_num):
    ans = ""
    num = int(str_num)
    while num >= 9:
        ans = str(num % 9) + ans
        num = num // 9
    return str(num) + ans

str_N = str(N)

for _ in range(K):
    str_N = replace8to5(convert10to9(convert8to10(str_N)))

print(str_N)