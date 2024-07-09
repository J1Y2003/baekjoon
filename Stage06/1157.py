import string

input_str = input()
input_str = input_str.lower()
max = -1
for alpha in string.ascii_lowercase:
    if (input_str.count(alpha) > max):
        max = input_str.count(alpha)
        max_alpha = alpha.upper()
    elif (input_str.count(alpha) == max):
        max_alpha = "?"

print(max_alpha)