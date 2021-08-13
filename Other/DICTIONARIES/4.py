your_text = input("Write something smart: ").split()
n = 1

my_dict = dict()
for i in your_text:
    my_dict[n] = i
    n += 1
print(my_dict)

for value in my_dict.values():
    print(value)
