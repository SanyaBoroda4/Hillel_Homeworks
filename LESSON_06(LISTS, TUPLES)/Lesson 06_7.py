import copy

x = [1, 3, 6, [1, 3]]
y = copy.deepcopy(x)

y[1][1] = 100


print(x)
print(y)
