matrix = [[1, 2, 3],
          [3, 4, 5],
          [6, 7, 8]
          ]
for i in range(len(matrix)):
    s = 0
    for j in range(len(matrix[i])):
        s += int(matrix[i][j])
    print(s)
