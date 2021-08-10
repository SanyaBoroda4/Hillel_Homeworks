import random

matrix = [random.randrange(100, 200, 10) for i in range(10)]

k = int(input("Enter index number from 0 to 9: "))
C = int(input("Enter a natural number between 100 & 200 multiple of 10: "))

if k not in range(0, 11):
    print("You have entered invalid index. Restart the program.")
else:
    if (C > 200 or C < 100) and C % 10 != 0 :
        print("You have entered invalid number. Restart the program.")
    else:
        matrix.append(C)
        for i in range(len(matrix) - 1, k, -1):
            matrix[i], matrix[i - 1] = matrix[i - 1], matrix[i]
