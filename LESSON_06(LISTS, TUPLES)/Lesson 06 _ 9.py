"""LIST CIM"""

arr = [1, 3, 4]
arr = [i * 2 for i in arr]
print(arr)

matrix = [1, 2, 3, 4]
matrix = [j * 10 for j in matrix if j % 2 == 0]
print(matrix)

"""_______________________________________________________________________________
"""

matrix_01 = [[1, 3], [10, 3], [42, 3]]
matrix_02 = [q * 10 for u in matrix_01 for q in u if q % 2 == 0]
print(matrix_02)
