def is_sorted(num_list):
    return all(num_list[i] <= num_list[i+1] for i in range(len(num_list -1)))
test_list_1 = [1, 2, 3, 4, 5]
test_list_2 = [1, 3, 2, 4, 5]