test_cases = int(input())
for _ in range(test_cases):
    try:
        repeat, input_str = input().split()
        print(*[int(repeat) * x for x in input_str], sep="")
    except ValueError:
        print("")