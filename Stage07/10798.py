matrix = []
vertical_line = ""
for _ in range(5):
    matrix.append([x for x in input()])
for column in range(15):
    for row in matrix:
        try:
            vertical_line += row[column]
        except:
            continue
print(vertical_line)