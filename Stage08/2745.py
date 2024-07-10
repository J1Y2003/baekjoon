import string

original_number, n_ary = input().split()
n_ary = int(n_ary)
unary = 0

for place, digit in enumerate(reversed(original_number)):
    if (digit in string.ascii_uppercase):
        digit = ord(digit) - 55
    else:
        digit = int(digit)
    unary += digit * (n_ary ** place)

print(unary)