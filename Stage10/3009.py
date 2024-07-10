x_list = []
y_list = []
x_coord, y_coord = 0, 0

for _ in range(3):
    a, b = [int(x) for x in input().split()]
    x_list.append(a)
    y_list.append(b)

for point in x_list:
    if (x_list.count(point) == 1):
        x_coord = point

for point in y_list:
    if (y_list.count(point) == 1):
        y_coord = point

print(x_coord, y_coord)