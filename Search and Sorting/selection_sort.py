def selection_sort(arr):

    # For every slot in array
    for fillslot in range(len(arr)-1, 0, -1):

        maxpos = 0

        # For every set of 0 to fillslot+1
        for location in range(1, fillslot+1):

            # Set maximum's location
            if arr[location] > arr[maxpos]:
                maxpos = location

        temp = arr[fillslot]
        arr[fillslot] = arr[maxpos]
        arr[maxpos] = temp


arr = [14, 46, 43, 27, 57, 41, 45, 21, 70]
selection_sort(arr)
print(arr)
