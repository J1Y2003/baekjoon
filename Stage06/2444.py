height = int(input())

for layer in range(1, height):
    print(" " * (height - layer), end="")
    print(("*" * (1 + (layer - 1) * 2)))
for layer in range(height, 0, -1):
    print(" " * (height - layer), end="")
    print(("*" * (1 + (layer - 1) * 2)))