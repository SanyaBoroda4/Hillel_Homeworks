def function(*args, x):
    if len(args) < 2:       # check whether there are at least two arguments to compare with 3rd one.
        return False

    for i in range(0, len(args)+1):
        for j in range(0, len(args)+1):
            if args[i] + args[j] == x:
                return True
            return False


print(function(4, 3, 4, 3, x=8))
print(function(1, 3, 4, 3, x=8))
