def insertion_sort(arr):

    # For every index in array
    for i in range(1, len(arr)):

        # Set current values and position
        currentvalue = arr[i]
        position = i

        # Sorted Sublist
        while position > 0 and arr[position-1] > currentvalue:

            arr[position] = arr[position-1]
            position = position-1

        arr[position] = currentvalue


arr = [3, 5, 4, 6, 8, 1, 2, 12, 41, 25]
insertion_sort(arr)
print(arr)
