# Binary Search on an ordered list using recursion
# Returns a boolean of True or False


def search(nums, target):

    # Base Case
    if len(nums) == 0:
        return False

    else:
        mid = len(nums)//2

        if nums[mid] == target:
            return True

        else:
            if target < nums[mid]:
                return search(nums[:mid], target)
            else:
                return search(nums[mid+1:], target)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

result = search(nums, 7)

print(result)
