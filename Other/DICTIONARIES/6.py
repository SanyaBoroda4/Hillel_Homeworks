dict1 = {1: 1, 2: 9, 3: 4}
sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get)

for w in sorted_keys:
    sorted_dict[w] = dict1[w]

print(sorted_dict)