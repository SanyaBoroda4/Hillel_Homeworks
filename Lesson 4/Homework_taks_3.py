num = input("Please enter a natural number: ")
for i in range(0, len(num) - 1, 1):
    if len(num) == 2 and num[0] == num[1]:
        print("YES")
        break
    elif num[i] == num[i - 1] or num[i] == num[i + 1]:
        print("YES")
        break
else:
    print("NO")
