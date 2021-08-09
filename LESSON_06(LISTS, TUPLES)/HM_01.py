matrix = [int(input()) for i in range(6)]

k = int(input("Please enter the index number from 0 to 5: "))

for i in range(k, len(matrix) - 1):
    matrix[i], matrix[i+1] = matrix[i+1], matrix[i]

matrix.pop()
