my_list = [1, 2.4, 4, "name", [1, 2, 3]]
for i in my_list:
    print(type(i), i)

print(len(my_list))
print(my_list.index(1))
print(id(my_list))
my_list.remove(4)
print(my_list)

print(id(my_list))

