def kadanes_algorithm(arr):
    curr_sum = 0
    max_sum = float('-inf')  # handles all-negative arrays

    for num in arr:
        curr_sum += num
        max_sum = max(curr_sum, max_sum)
        if curr_sum < 0:
            curr_sum = 0

    return max_sum