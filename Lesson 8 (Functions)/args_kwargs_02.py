def f(*args):
    s = 0
    for i in args:
        s += i
    return s


print(f(1, 2, 3))
