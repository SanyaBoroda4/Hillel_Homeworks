import random


def num_generator(x, y):
    return random.randint(x, y)


for i in range(1, 100):
    print(num_generator(1, 10), end=" ")
