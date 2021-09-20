def min_cont_sum(arr):

    breakpoint()

    if len(arr) == 0:
        return 0

    min_sum = current_sum = arr[0]

    for num in arr[1:]:

        current_sum = min(current_sum+num, num)

        min_sum = min(current_sum, min_sum)

    return min_sum


sum = min_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])

print(sum)
