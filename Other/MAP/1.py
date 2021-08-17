from random import randint

a = [randint(-10, -1) for i in range(0, 10)]
print(a)
b = map(abs, a)
print(tuple(b))


def f(x):
    return x ** 2


y = map(f, a)
print(list(y))
