import array

"""
Create temp_number 2d array with m columns and d strings where each element is equal to 0
"""


def matrix_2d(m, d):
    matrix = []
    for i in range(m):
        internal_array = []

        for j in range(d):
            internal_array.append(0)

        matrix.append(internal_array)

    return matrix


test_matrix = matrix_2d(4, 2)
for array in test_matrix:
    for el in array:
        print(el, end=" ")
    print()
