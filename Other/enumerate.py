my_string = "ABCD"
for i in enumerate(my_string, 10):
    print(i)

my_list = [10, 11, 12]
for index, val in enumerate(my_list):
    my_list[index] += 10
print(my_list)

d = {"hello": 1, "worlds": 2}
for i in enumerate(d):
    print(i)

