a = []
n = int(input("Please enter row quantity: "))
m = int(input("Please enter column quantity: "))

for i in range(n):
    b = []
    for j in range(m):
        b.append(int(input("Please input element of matrix: ")))
    a.append(b)
print(a)
