# def fun1(a, c=2, b=3):
#     print(a + c + b)
#
#
# fun1()


def solve(s):
    c = []
    for i in range(len(s) - 1):
        if i % 2 == 0:
            c.append(s[i])
    return c


print(solve([1, 2, 4, 5, 6, 7, 8]))
