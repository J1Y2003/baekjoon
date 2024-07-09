paper = [[0 for _ in range(100)] for _ in range(100)]
N = int(input())
for _ in range(N):
    left, bottom = [int(x) for x in input().split()]
    for column in range(left, left + 10):
        for row in range(bottom , bottom + 10):
            paper[row][column] = 1

total = 0
for row in paper:
    total += sum(row)
print(total)