n = int(input("strings: "))
m = int(input("columns: "))

x = [[i * j for i in range(n)] for j in range(m)]
for i in x:
    print(i)

