matrix = [[1, 2, 3],
          [3, 4, 5],
          [6, 7, 8]
          ]
for i in matrix:
    for j in i[::-1]:
        print(j, end=" ")
    print()
