input_str = input()
alphabet_array = [-1] * 26

for idx, letter in enumerate(input_str):
    letter_ascii = ord(letter) - 97
    if (alphabet_array[letter_ascii] == -1):
        alphabet_array[letter_ascii] = idx

print(*alphabet_array)