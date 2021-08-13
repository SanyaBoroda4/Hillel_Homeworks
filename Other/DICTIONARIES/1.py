dict_01 = {
    "Odesa": 482,
    "Kyiv": 9482,
    "Lviv": 32
}
print(dict_01)

my_dict = dict(x=4, y=6)
print(my_dict)

my_dict_01 = dict.fromkeys(["a", "b", "c"], 100)
print(my_dict_01)

my_dict_02 = {a: a**2 for a in range(10)}
print(my_dict_02)

empty = {}
print(empty, type(empty))