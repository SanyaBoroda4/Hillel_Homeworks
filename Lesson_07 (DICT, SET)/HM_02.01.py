from collections import Counter


your_text = input("Write something smart: ")
adjusted_text = your_text.replace(";", "").replace(",", " ").\
    replace(".", " ").replace("!", " ")
text_to_list = adjusted_text.lower().split()

n = 1

my_dict = dict()
for i in text_to_list:
    my_dict[n] = i
    n += 1
print(my_dict)

result = Counter(my_dict.values())
print(dict(result))
