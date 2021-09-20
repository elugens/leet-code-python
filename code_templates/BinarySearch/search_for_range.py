# THIS IS NOT COMPLETE NEED TO FINISH
# Search for Range / nums = [5,7,7,8,8,10], target = 8


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)

        if left < 0 and right < len(nums):
            return [-1, -1]

        while left < right:
            mid = (left + right)//2

            if nums[mid] > target or (left and target == nums[mid]):
                left = mid

            else:
                right = mid+1

        return lo
