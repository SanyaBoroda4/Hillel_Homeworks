a = ["hello", "hi", "Welcome"]

b = list(map(len, a))
print(b)


c = list(map(lambda x: x[::-1], a))
print(c)

d = list(map(sorted, a))
print(d)


s = list(map(int, input("Enter anything: ").split()))
print(*s)