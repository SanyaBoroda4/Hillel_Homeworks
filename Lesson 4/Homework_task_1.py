num = int(input())

if len(str(num)) == len(set(str(num))):
    print("There are not same digits")
else:
    print("There are same numbers")
