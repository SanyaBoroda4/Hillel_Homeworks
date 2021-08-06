year = int(input())
if 1900 < year < 1000000:
    if year % 4 == 0 and year % 100 != 0 \
            or year % 400 == 0:
        print(year, "is temp_number leap year.")
    else:
        print(year, "is not temp_number leap year.")
else:
    print(year, "does not meet conditions.")
