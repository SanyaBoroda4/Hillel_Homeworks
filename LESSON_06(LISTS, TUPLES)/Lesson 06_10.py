"""Expression comprehension"""


list = [1, 3, 5, 8, 12]
my_expr = sum(i for i in list if i % 2 == 0) # only works for 1 TIME!!!
print(my_expr)
