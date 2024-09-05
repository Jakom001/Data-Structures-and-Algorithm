def selection_sort(num_list):
    n = len(num_list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if num_list[j] < num_list[min_index]:
                min_index = j
                num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    return num_list

num_list = [20,11,23,44,5,20]

print(f"unsorted list: {num_list}")

sorted_list = selection_sort(num_list)

print(f"sorted list: {sorted_list}")
