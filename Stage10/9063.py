max_x, max_y = -10001, -10001
min_x, min_y = 10001, 10001

for _ in range(int(input())):
    x, y = [int(x) for x in input().split()]
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    min_x = min(x, min_x)
    min_y = min(y, min_y)

print((max_x - min_x) * (max_y - min_y))