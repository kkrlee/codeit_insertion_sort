def insertion_sort(my_list):
    for i in range(len(my_list)):
        key = my_list[i]

        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j  + 1] = key
    
some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
print(some_list)
