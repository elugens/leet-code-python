# Ordered List Sequential Search


def ordered_seq_search(arr, ele):
    """
    Input array must be ordered / sorted for this to work

    """

    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:

        if arr[pos] == ele:
            found = True
            print(ele)
        else:
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1

    return found


arr = [1, 2, 3, 4, 5, 6]

print(ordered_seq_search(arr, 3))
