import array

matrix = [[1, 3, 5],
          [4, 3, 21],
          [3, 5, 9]
          ]
print(list)

print()

for array in matrix:
    for el in array:
        print(el, end=" ")
    print()

print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
