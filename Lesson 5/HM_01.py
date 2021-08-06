rows = input("Please enter temp_number number between 3 & 9: ")
if rows.isdigit():
    rows = int(rows)
    if 2 < rows < 10:
        for i in range(1, rows + 1):
            matrix = []

            for j in range(1, i+1):
                j = str(j)      # перед тем как наполнять пустой массив элементами int, преобразовал в str назад.
                matrix.append(j)

            new_matrix = matrix + matrix[-2::-1]
            pyramide = "".join(new_matrix)
            print(pyramide)

    else:
        print("Restart the program and enter temp_number number within 3 - 9!")
else:
    print("Restart the program and enter temp_number NUMBER!")
