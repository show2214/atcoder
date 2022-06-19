N = int(input())
c = i = 1

while i < 5e6:
    i += 1
    while N % i < 1:
        N /= i
        c -= 1

c -= N > 1

print(c.bit_length())