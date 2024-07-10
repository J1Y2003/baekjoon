import math

climb, fall, height = [int(x) for x in input().split()]
days = math.ceil((height - climb) / (climb - fall))
print(days + 1)