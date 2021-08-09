import random


# a = [int(input()) for i in range(4)]
# print(a)

b = [random.randint(10, 50) for i in range(6)]
print(b)

z = input().split()
z = [int(i) for i in z]
print(z)