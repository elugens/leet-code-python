# Binary Search on an ordered list using recursion


def rec_bin_search(arr, ele):

    # base case
    if len(arr) == 0:
        return False

    # Recursive Case
    else:

        mid = len(arr)//2

        # If match found
        if arr[mid] == ele:
            return True

        else:

            # Call again on second half
            if ele < arr[mid]:
                return rec_bin_search(arr[:mid], ele)

            # Or call on first half
            else:
                return rec_bin_search(arr[mid+1:], ele)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

result = rec_bin_search(arr, 5)

print(result)
