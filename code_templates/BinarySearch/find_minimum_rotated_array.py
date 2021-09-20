# Find Minimum in Rotated Sorted Array [4,5,6,7,0,1,2]


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums)-1

        # base case - find out if nums has only one value at index 0
        # return that number as the minimum
        if len(nums) == 1:
            return nums[0]

        # Edge case - if last number is greater than the number at index 0
        # return that num index 0 as the minimum
        if nums[right] > nums[0]:
            return nums[0]

        # Binary Search
        while right >= left:
            # Set the mid point
            mid = left + (right - left)//2

            # if left nums are greater than the right return the right
            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]

            # if right nums are greater that the left return left
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if left nums are greater nums on the right than the smallest element is on the right
            if nums[mid] > nums[0]:
                left = mid + 1

            # Once you get here you should have the smallest element
            else:
                right = mid - 1
