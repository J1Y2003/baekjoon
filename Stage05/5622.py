alpha_to_number = {
    "ABC" : 2, "DEF" : 3, "GHI" : 4,
    "JKL" : 5, "MNO" : 6, "PQRS" : 7,
    "TUV" : 8, "WXYZ" : 9
}
alpha_number = input()
total = 0

for alpha in alpha_number:
    for alpha_list in alpha_to_number.keys():
        if alpha in alpha_list:
            alpha = alpha_list
    total += alpha_to_number[alpha] + 1

print(total)