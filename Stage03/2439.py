height = int(input())

for i in range(1, height + 1):
    line = "*" * i
    print(line.rjust(height))