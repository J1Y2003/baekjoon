a, b, c = [int(x) for x in input().split()]
options = []
if a + b <= c:
    print(2 * (a + b) - 1)
elif a + c <= b:
    print(2 * (a + c) - 1)
elif b + c <= a:
    print(2 * (b + c) - 1)
else:
    print(a + b + c)