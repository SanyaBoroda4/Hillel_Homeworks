import random


k = int(input("Please enter element quantity for matrix: "))

matrix_01 = [random.randint(0, 5) for i in range(k)]
matrix_02 = [random.randint(0, 5) for j in range(k)]

unique_elements = len(set(matrix_01 + matrix_02))
