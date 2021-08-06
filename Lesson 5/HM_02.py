import random


num = random.randint(0, 100)
count = 0
your_number = -1
while your_number != num:
    temp_number = input("Please enter temp_number number from 0 to 100: ")
    count += 1
    if temp_number.isdigit():
        your_number = int(temp_number)
        if your_number < 0 or your_number > 100:
            print("Number should be in range 0-100")
            continue
        if your_number < num:
            print("Your number is less!")
        elif your_number > num:
            print("Your number is bigger!")
    else:
        print("You have entered wrong symbols. Only numbers should be entered.")
else:
    print(f"Congrats! You have quessed the number {num}! You have used {count} attempts.")
