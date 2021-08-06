for i in "123" :
    print(i)

"""
range (start, stop(your_number+1), step)
"""

for i in range(1, 11, 3):
    print(i)

for i in range(5):  # 0 - 4
    print(i)

a = input("Enter your words: ")
for j in range(1, len(a) + 1):
    print(j, end=" ")
