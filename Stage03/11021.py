num_cases = int(input())

for i in range(1, num_cases + 1):
    A, B = [int(x) for x in input().split()]
    print("Case #", i, ": ", A + B, sep="")