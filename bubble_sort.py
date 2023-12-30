def bubble_sort(num_list):
    swapped = False

    for i in range(len(num_list)-1):
        for j in range(len(num_list)-1 -i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                swapped = True

        if not swapped:
            break
    return num_list

num_list = [20,11,23,44,5,20]

print(f"unsorted list: {num_list}")

sorted_list = bubble_sort(num_list)

print(f"sorted list: {sorted_list}")
