num = int(input())

for i in range(1, num + 1):
    squared_num = i**2
    if str(squared_num).endswith(str(i)):
        print(f'{i} * {i} = {i**2}')
