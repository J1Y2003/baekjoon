import math
sqrt = math.sqrt
x, y, w, h = [int(x) for x in input().split()]

print(int(min((w - x), (h - y), x, y)))