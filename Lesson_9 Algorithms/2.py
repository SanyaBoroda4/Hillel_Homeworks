def binary_search(sequence, look_for):
    i = 0
    j = len(sequence) - 1

    while i < j:
        middle = (i + j) // 2
        if look_for > sequence[middle]:
            i = middle + 1
        else:
            j = middle

    if sequence[j] ==look_for:
        return j
    else:
        return None


print(binary_search([1, 2, 3, 4, 5, 6], 3))
