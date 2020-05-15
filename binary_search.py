def binary_search(lst, num):
    low = 0
    high = len(lst) - 1

    while low <= high:
        middle = (low + high) // 2
        print(f'New value of low - {low} and high- {high}')
        print(f'Middle value - {middle}')
        if lst[middle] == num:
            return middle
        elif lst[middle] < num:
            low = middle + 1
        elif lst[middle] > num:
            high = middle - 1
    return -1

lst = [2,3,5,7,8,9,12,45,67,70]
print(binary_search(lst, 70))