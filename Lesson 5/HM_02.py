import random


num = random.randint(0, 100)
count = 0
n = -1
while n != num:
    a = input("Please enter a number from 0 to 100: ")
    count += 1
    if a.isdigit():
        n = int(a)
        if n < 0 or n > 100:
            print("Number should be in range 0-100")
            continue
        if n < num:
            print("Your number is less!")
        elif n > num:
            print("Your number is bigger!")
    else:
        print("You have entered wrong symbols. Only numbers should be entered.")
else:
    print(f"Congrats! You have quessed the number {num}! You have used {count} attempts.")
