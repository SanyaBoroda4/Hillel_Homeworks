def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-2, i-1, -1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


lst = [3, 90, 54, 33, 1, -2]
another_list = [3, 90, 54, 33, 1, -2]

bubble_sort(lst)
print(lst)

