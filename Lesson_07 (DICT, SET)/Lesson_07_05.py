"SETS"

a = {1, 3, 5}
b = {2, 3, 1}
c = a | b
print(c)

c_01 = a.intersection(b)
print(c_01)

difference = a - b
print(difference)

difference_01 = a.difference(b)
print(difference_01)

y = a ^ b
print(y)