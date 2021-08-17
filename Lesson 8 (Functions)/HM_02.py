from random import randint


my_list = [randint(10, 20) for i in range(1, 10)]

num_pow = list(map(lambda x, y=2: x ** y, my_list))
print(num_pow)
