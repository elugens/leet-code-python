def shell_sort(arr):

    sublistcount = len(arr)//2

    while sublistcount > 0:
        for start in range(sublistcount):

            gap_insertion_sort(arr, start, sublistcount)

        print('After increments of size: ', sublistcount)
        print('The list is ', arr)

        sublistcount = sublistcount//2


def gap_insertion_sort(arr, start, gap):

    for i in range(start+gap, len(arr), gap):
        currentvalue = arr[i]
        position = i

        while position >= gap and arr[position-1] > currentvalue:
            arr[position] = arr[position-gap]
            position = position-gap

        arr[position] = currentvalue


arr = [45, 67, 23, 45, 21, 24, 7, 2, 6, 4, 90]
shell_sort(arr)
print(arr)
