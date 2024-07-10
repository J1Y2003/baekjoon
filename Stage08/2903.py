length = 2
add = 1
for _ in range(int(input())):
    length += add
    add *= 2

print(length ** 2)