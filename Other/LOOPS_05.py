"""multiplication table"""

for j in range(1, 11):
    for i in range(1, 11):
        print(f"{i} * {j} = {i*j}", end=" ")
    print()