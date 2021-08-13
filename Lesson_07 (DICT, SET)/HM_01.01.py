import random


matrix = [random.randint(0, 100) for i in range(50)]

print(f"The total number of different numbers is {len(set(matrix))}.")
