import string

def place_finder (number, n_ary):
    place = 0
    while (number >= (n_ary ** place)):
        place += 1
    return place

unary_number, n_ary = [int(x) for x in input().split()]
n_ary = int(n_ary)
place = place_finder(unary_number, n_ary)
n_ary_number = [0] * place

while (place > 0):
    n_ary_number[place - 1] = int(unary_number / (n_ary ** (place - 1)))
    unary_number = unary_number % (n_ary ** (place - 1))
    place -= 1

for idx, digits in enumerate(n_ary_number):
    if (digits >= 10):
        n_ary_number[idx] = chr(digits + 55)

print(*reversed(n_ary_number), sep="")