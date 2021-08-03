"""STRINGS"""

S = r"C:\DRIVERS\ASUS System Control Interface V2"  # Подавляет экранирование
print(S)

b = "Hello How are you!"
print(b[2:4])       # обращение по индексу
print(b[:5])

print(b[0:5:2])     # извлечение среза

print(b[::-1])      # инверсия


print(b.isalnum())
print(b.isalpha())
print(b.isalnum())
print(b.upper())
print(b.index("are"))

print(b.split())
