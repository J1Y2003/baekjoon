input_str = input()
if (len(input_str) % 2 == 0):
    center = int(len(input_str)/2)
    palindrome = int((center == sum([a == b for a, b in zip(input_str[center:], reversed(input_str[:center]))])))
    print(palindrome)
else:
    center = int(len(input_str)/2)
    palindrome = int((center == sum([a == b for a, b in zip(input_str[center + 1:], reversed(input_str[:center]))])))
    print(palindrome)