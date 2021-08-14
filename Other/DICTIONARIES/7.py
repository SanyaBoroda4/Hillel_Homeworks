import operator


dict = {1: 4,
        2: 9,
        4: 11,
        3: 3
        }

get_item_max = operator.itemgetter(max(dict))
print(get_item_max(dict))
