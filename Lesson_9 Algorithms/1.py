def linear_search(sequence, look_for) :
    i = 0
    length = len(sequence)

    while i < length and look_for != sequence[i] :
        i += 1

    return i if i < length else None


print(linear_search([1, 2, 3, 5], 10))
print(linear_search([1, 2, 3, 5], 3))

""""________________________________________________________________________"""


def linear_search_py(seQuence, search):

    return seQuence.index if search in seQuence else None

