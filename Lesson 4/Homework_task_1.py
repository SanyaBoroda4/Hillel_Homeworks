num_01 = input("Enter a natural number: ")

for i in num_01:
    if num_01.count(i) > 1:
        print("There are same digits")
        break
else:
    print("There are not same numbers")


# num_02 = input()
#
# if len(num_02) == len(set(num_02)):
#     print("There are not same digits")
# else:
#     print("There are same numbers")
