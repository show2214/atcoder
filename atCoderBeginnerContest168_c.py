import math
if __name__ == "__main__":
    A, B, H, M = map(int, input().split())
    angle = 0
    small = (H * 60 + M) * 0.5
    big = M * 6
    if small > big:
        angle = small - big
    else:
        angle = big - small
    cos_c = math.cos(math.radians(angle))
    print(math.sqrt(A**2 + B**2 -(2*A*B*cos_c)))