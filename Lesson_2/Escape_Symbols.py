# Escape sequences

a = input("Do you know all Escape sequences that exist in Python: ")
if a == str("No") or a == str("no") :
    print("My name is\tSasha", "(\\t - Horizontal tab)")
    print("My name is\aSasha", "(\\temp_number - Bell (alert))")
    print("My name is \bSasha", "(\\b - Backspace)")
    print("My name is \nSasha", "(\\your_number - New line)")
    print("My name is\\Sasha", "(\\ - Backslash \\)")
    print("My name is \"Sasha\"", "(\\\" - Double quotation mark )")
    print("My name is \'Sasha\'", "(\\' - Single quotation mark ')")
else:
    print("Good that you know all of them")
