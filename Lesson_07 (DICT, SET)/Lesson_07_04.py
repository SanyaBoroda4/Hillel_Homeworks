"SETS"

a = set("Hello!")
print(a)


for item in {1, 2, "some"}:
    print(item)

a = {"Sasha", "Dima"}
name = input("")
if name in a:
    a.remove(name)
print(a)