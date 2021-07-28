password = "12345"
a = "temp"
attempt = 0
while attempt < 3 and a != password:
    a = input("Please enter password: ")
    if a != password:
        attempt += 1
        print("Wrong password")
    else:
        print("Access granted")
if attempt == 3:
    print("You have run ouf of attempts to input password")
