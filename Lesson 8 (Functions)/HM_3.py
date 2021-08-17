import random


def num_generator(x, y):
    for i in range(1, 100):
        z = random.randint(x, y)
        yield z


for j in num_generator(1, 10):
    print(j, end=" ")
