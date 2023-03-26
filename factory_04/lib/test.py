from math import cos, sin, pi

n = 8
fi = 360 / n

x0 = 15
y0 = 15
r = 25


def get_coords(x0: float, y0: float, r: float, fi: float, i, n) -> tuple:
    x = x0 + r * cos(fi + (2 * pi * i)/n)
    y = y0 + r * sin(fi + (2 * pi * i)/n)
    return x, y


for i in range(1, n + 1):
    x, y = get_coords(x0, y0, r, fi, i, 8)
    print(f'x = {x}  y = {y}')
