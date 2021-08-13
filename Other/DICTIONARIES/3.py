dict_01 = {
    "Odesa": 482,
    "Kyiv": 9482,
    "Lviv": 32
}

del dict_01["Lviv"]
print(dict_01)

print(len(dict_01))

print("Lviv" not in dict_01)

for key in dict_01:
    print(key, dict_01[key])
