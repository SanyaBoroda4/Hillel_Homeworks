a, *b, c = [1, 2, 3, 4, 1, 2, 5]

print(b)
print(a)

print(a, b, c)

*x, y, z = [2, 3]
print(x, y, z)

o = range(5)
print(*o, type(o))
