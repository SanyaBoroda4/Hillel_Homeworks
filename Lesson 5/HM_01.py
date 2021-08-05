rows = input("Please enter a number between 3 & 9: ")
if rows.isdigit():
    rows = int(rows)
    if 2 < rows < 10:
        for i in range(1, rows + 1):
            matrix = []

            for j in range(1, i+1):
                matrix.append(j)

            new_matrix = matrix + matrix[-2::-1]
            print(new_matrix)
    else:
        print("Restart the program and enter a number within 3 - 9!")
else:
    print("Restart the program and enter a NUMBER!")
