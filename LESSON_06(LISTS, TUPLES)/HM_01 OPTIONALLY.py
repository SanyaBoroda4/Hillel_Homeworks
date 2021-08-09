import random


a = [random.randint(0, 100) for i in range(10)]

k = int(input("Please enter the index number from 0 to 9: "))

a = a[:k] + a[k+1:] + [k]
a.pop()
