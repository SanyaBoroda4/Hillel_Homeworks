import random


matrix_01 = [random.randint(0, 100) for i in range(50)]
matrix_02 = [random.randint(0, 100) for j in range(50)]

total_different_elements = len(set(matrix_01 + matrix_02))
