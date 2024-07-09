import string

N = int(input())
total = 0

for _ in range(N):
    input_str = input()
    i = 0
    cur = ord(input_str[i]) - 97
    alphabets = [0] * 26
    flag = 0

    while (i < len(input_str)):
        letter_ascii = ord(input_str[i]) - 97
        if (letter_ascii != cur):
            if (alphabets[letter_ascii] == 1):
                flag = 1
                break
            else:
                alphabets[cur] = 1
            cur = letter_ascii
            i += 1
        else:
            i += 1
            
    if (flag == 0):
        total += 1

print(total)