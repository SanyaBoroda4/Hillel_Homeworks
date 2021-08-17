def squared(x):
    return x ** 2


a = squared(squared(10))
print(a)


def even_number(x):
    return x % 2 == 0
    # if x % 2 == 0:
    #     return True
    # return False


for i in range(1, 11):
    print(i, even_number(i))
