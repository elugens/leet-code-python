"""
Template #1 is the most basic and elementary form of Binary Search. 
It is the standard Binary Search Template that most high schools or universities use when they first teach students computer science.
Template #1 is used to search for an element or condition which can be determined by accessing a single index in the array.

"""


def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # Base Case
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1

    # Iteration with Divide and Conquer
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]

result = binarySearch(nums, 4)

print(result)
