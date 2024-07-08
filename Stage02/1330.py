input_str = input()
A, B = input_str.split()
A = int(A)
B = int(B)
if (A > B):
    print(">")
elif (A < B):
    print("<")
else:
    print("==")