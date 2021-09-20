# Binary Search on an orderd list
def search(nums, target):

    first = 0
    last = len(nums)-1

    found = False

    while first <= last and not found:

        mid = (first+last)//2

        if nums[mid] == target:
            found = True
        else:
            if target < nums[mid]:
                last = mid-1
            else:
                first = mid+1

    return found


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

result = search(nums, 21)

print(result)
