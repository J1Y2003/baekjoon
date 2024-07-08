import sys

test_cases = int(input())

for _ in range(test_cases):
    input_str = sys.stdin.readline()
    A, B = [int(x) for x in input_str.rstrip().split()]
    print(A + B)