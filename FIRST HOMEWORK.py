x = int(input())    # days quantity ran on the first day
y = int(input())    # days quantity ran on the input day
k = 1               # days quantity
while x < y:
    k += 1          # next day
    x *= 1.1        # distance ran each day increased by 10%
print(k)
