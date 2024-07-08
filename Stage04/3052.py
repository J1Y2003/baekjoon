num_set = set()
remainder_set = set()

for _ in range(10):
    num = int(input())
    num_set.add(num)

for numbers in num_set:
    remainder_set.add(numbers % 42)

print(len(remainder_set))