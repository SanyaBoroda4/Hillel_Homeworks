def function(*args, x):
    if len(args) < 2:       # check whether there are at least two arguments to compare with 3rd one.
        return False

    for i in args:
        for j in args:
            if i + j == x:
                return True
            return False


print(function(2, 3, 4, 1, x=4))
