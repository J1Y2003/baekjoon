x = int(input())
y = int(input())

x_is_positive = (x > 0)
y_is_positive = (y > 0)

if (x_is_positive and y_is_positive):
    print("1")
elif (x_is_positive):
    print("4")
elif (y_is_positive):
    print("2")
else:
    print("3")