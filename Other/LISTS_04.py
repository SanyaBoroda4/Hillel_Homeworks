"""
From        to
1 2 3       3 2 1
4 5 6       6 5 4
7 8 9       9 8 7
"""
import array

def swap(array_2d, i, j):
    temp = array_2d[i]
    array_2d[i] = array_2d[j]
    array_2d[j] = temp

def mirrored_2d_array(array_2d):
    array_2d = []
    for array in array_2d:
        for i in range(len(array_2d) // 2):
            swap(array_2d, i, len(array_2d) - 1 - i):

