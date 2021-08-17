def example(**kwargs) :
    return kwargs


print(example(a=1, b=2, c=3, d=4, z=5))


def combined(*args, **kwargs) :
    print(args, kwargs)


combined(1, 2, 3, 3, a=2, c=1)
