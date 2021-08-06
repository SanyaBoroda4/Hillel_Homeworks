a = [1, 3, 5]
b = a.copy()
print(b)

b[1] = 1000
print(a, b)

b = a[:]
print(b)