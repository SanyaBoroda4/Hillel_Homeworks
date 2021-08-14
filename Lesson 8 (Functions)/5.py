f1 = lambda: 10 + 20
f2 = lambda x, y: x + y
f3 = lambda x, y, z: print(f1())


print(f1())
print(f3(4, 10, 30))


f = lambda x, y = 2: x + y
print(f(5, 5))
print(f(10))

