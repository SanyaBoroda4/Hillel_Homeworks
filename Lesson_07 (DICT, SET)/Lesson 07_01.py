student = {
    "name": "Sasha",
    "age": 28,
    "hobby": ["football", "karting", "poker"],
    "brother": {
        "name": "Dimon",
        "age": 36
    }
}

car = dict()

"""dictionary comprehension"""
d = {a: a**2 for a in range(7)}
print(d)

"""fromkeys"""

my_dict = dict.fromkeys(["a", "b"], 100)
