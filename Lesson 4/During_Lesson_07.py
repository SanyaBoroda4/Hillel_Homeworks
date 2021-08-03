"""f-string"""


d = {
    "name": "Alex",
    "surname": "Sorokin",
    "gender": "male",
    "amount": 3342
}

final_text = f'Dear {d["name"]} {d["surname"]}, your current amount of money is {d.get("amount")}$.'

print(final_text)




