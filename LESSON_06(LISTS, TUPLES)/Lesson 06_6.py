z = [1, 2, 100]
y = list(z)
x = z[:]
p = z.copy()

print(id(x))
print(id(y))
print(id(z))
print(id(p))
