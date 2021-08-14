def gen_f(x, y):
    for i in range(1, x +1):
        yield i ** y


# for n in gen_f(10, 2):
#     print(n, end="")

f = gen_f(4, 2)

print(f.__next__())
print(f.__next__())
print(f.__next__())

