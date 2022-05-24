T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

import math

W = 2*math.pi / T

for _ in range(Q):
    E = int(input())
    sy = -(L/2) * math.sin(W * E)
    sz = L/2 - (L/2) * math.cos(W * E)
    a = sz / ((X**2 + (sy - Y)**2))**0.5
    rad = math.atan(a)
    deg = math.degrees(rad)
    print(deg)