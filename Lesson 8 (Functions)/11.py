def factorial(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f


for j in range(1, 11):
    print(j, factorial(j))
