import random


k = int(input("Please enter element quantity for matrix: "))

matrix_01 = [random.randint(0, 5) for i in range(k)]
matrix_02 = [random.randint(0, 5) for j in range(k)]


unique_elements = len(list(i for i in range(len(matrix_01 + matrix_02)) if (matrix_01+matrix_02).count(i) == 1))
