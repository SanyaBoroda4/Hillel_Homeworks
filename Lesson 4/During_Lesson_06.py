"""f-string"""

name = "Alex"
surname = "Sorokin"
gender = "male"


def balance(x):
    return x**2


final_text = f"Hello, Dear {name.upper()} {surname.upper()}. Your balance is {balance(8)} $."

print(final_text)

