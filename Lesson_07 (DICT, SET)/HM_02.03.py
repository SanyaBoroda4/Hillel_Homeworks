import operator


your_text = """
The former seems to be much the more important; 
for nearly similar variations sometimes arise under, 
as far as we can judge, dissimilar conditions; 
and, on the other hand, dissimilar variations arise under conditions 
which appear to be nearly uniform. The effects on the offspring are either
definite or in definite. They may be considered as definite when all 
or nearly all the offspring of individuals exposed to certain conditions 
during several generations are modified in the same manner. 
It is extremely difficult to come to any conclusion in regard to the
extent of the changes which have been thus definitely induced.
"""

adjusted_text = your_text.replace(";", "").replace(",", " ").\
    replace(".", " ")
text_to_list = adjusted_text.lower().split()
my_dict = dict()

for item in text_to_list:
    if item in my_dict:
        my_dict[item] += 1
    else:
        my_dict[item] = 1

print(max(my_dict, key=my_dict.get))

"""below I did sorting just for training"""
sorted_dict = {}
sorted_keys = sorted(my_dict, key=my_dict.get, reverse=True)

for w in sorted_keys:
    sorted_dict[w] = my_dict[w]

print(max(sorted_dict, key=sorted_dict.get))

