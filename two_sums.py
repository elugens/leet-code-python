'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Input: [1, 3, 2, 2], 4

Output: [0,1]
'''


class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if (target - nums[i] in nums) and (not nums.index(target - nums[i]) == i):
                return [i, nums.index(target - nums[i])]


total = Solution()

print(total.twoSum([1, 3, 2, 2], 4))
